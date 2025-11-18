WITH ranked_keywords AS (
    -- 1) Ranqueia palavras-chave por post, priorizando maior SV e melhor posição
    SELECT
        c.post_name,
        c.keyword,
        c.sv,
        c.position,
        ROW_NUMBER() OVER (
            PARTITION BY c.post_name
            ORDER BY c.sv DESC, c.position ASC
        ) AS keyword_rank
    FROM cpv_semrush AS c
    WHERE c.position < 10
),

semrush_keywords AS (
    -- 2) Mantém até 10 palavras-chave principais por post, agregadas em um array
    SELECT
        rk.post_name,
        ARRAY_AGG((rk.keyword, rk.sv, rk.position)) AS keywords_semrush
        -- Se preferir algo mais “legível”, considere:
        -- jsonb_agg(jsonb_build_object('keyword', rk.keyword, 'sv', rk.sv, 'position', rk.position)) AS keywords_semrush
    FROM ranked_keywords AS rk
    WHERE rk.keyword_rank <= 10
    GROUP BY rk.post_name
),

sessions_with_docs AS (
    -- 3) Junta sessões com documentos e palavras-chave, já calculando a data da sessão
    SELECT
        TO_DATE(SUBSTRING(s.datehourminute FROM 1 FOR 8), 'YYYYMMDD') AS session_date,
        s.sessions,
        s.source_medium,
        s.path,
        d.post_name,
        d.title,
        d.paragraph,
        d.ngrams,
        sk.keywords_semrush
    FROM sessions_cpv AS s
    JOIN documents_cpv AS d
        ON d.post_name = split_part(s.path, '/', 4)
    JOIN semrush_keywords AS sk
        ON d.post_name = sk.post_name
    WHERE TO_DATE(SUBSTRING(s.datehourminute FROM 1 FOR 8), 'YYYYMMDD') >= DATE '2023-05-01'
      -- Estes filtros hoje são sempre verdadeiros; ajuste para filtros reais se necessário
      AND LOWER(d.paragraph) LIKE '%%'
      AND LOWER(d.title) LIKE '%%'
),

post_sessions_ngrams AS (
    -- 4) Consolida sessões por post + título + ngrams + keywords
    SELECT
        swd.post_name,
        swd.title,
        swd.ngrams,
        swd.keywords_semrush,
        SUM(swd.sessions) AS total_sessions
    FROM sessions_with_docs AS swd
    GROUP BY
        swd.post_name,
        swd.title,
        swd.ngrams,
        swd.keywords_semrush
),

top_posts AS (
    -- 5) Seleciona os 500 posts com mais sessões (para limitar o escopo da análise)
    SELECT
        psn.post_name,
        psn.title,
        psn.ngrams,
        psn.keywords_semrush,
        psn.total_sessions
    FROM post_sessions_ngrams AS psn
    ORDER BY psn.total_sessions DESC
    LIMIT 500
),

sources_by_post_date AS (
    -- 6) Reabre as sessões por fonte, post e data apenas para os top 500 posts
    SELECT
        s.source_medium,
        split_part(s.path, '/', 4) AS post_name_ga,
        TO_DATE(SUBSTRING(s.datehourminute FROM 1 FOR 8), 'YYYYMMDD') AS session_date,
        s.sessions
    FROM sessions_cpv AS s
    WHERE split_part(s.path, '/', 4) IN (
        SELECT tp.post_name FROM top_posts AS tp
    )
),

post_daily_sessions AS (
    -- 7) Consolida sessões diárias por post
    SELECT
        spd.post_name_ga AS post_name,
        spd.session_date,
        SUM(spd.sessions) AS daily_sessions
    FROM sources_by_post_date AS spd
    GROUP BY
        spd.post_name_ga,
        spd.session_date
),

post_weekly_sessions AS (
    -- 8) Consolida sessões semanais por post (função get_week_number é assumida como já criada)
    SELECT
        pds.post_name,
        get_week_number(pds.session_date) AS week_number,
        SUM(pds.daily_sessions) AS weekly_sessions
    FROM post_daily_sessions AS pds
    WHERE pds.session_date > DATE '2023-02-25'
    GROUP BY
        pds.post_name,
        get_week_number(pds.session_date)
),

post_weekly_window AS (
    -- 9) Cria a janela de semanas (11 a 18) com LEAD para comparar evolução
    SELECT
        pws.post_name,
        pws.week_number,
        pws.weekly_sessions AS week11,
        LEAD(pws.weekly_sessions, 1) OVER (
            PARTITION BY pws.post_name ORDER BY pws.week_number
        ) AS week12,
        LEAD(pws.weekly_sessions, 2) OVER (
            PARTITION BY pws
