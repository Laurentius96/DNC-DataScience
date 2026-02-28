import streamlit as st
import pickle
import numpy as np

# 1. Carregar o modelo de fraude previamente treinado
with open('modelo_fraude.pkl', 'rb') as file:
    fraud_model = pickle.load(file)

st.title("Detecção de Fraude em Transações")
st.write("Este aplicativo utiliza um modelo de Regressão Logística para prever se uma transação é fraudulenta.")

# 2. Capturando informações da transação
st.header("Detalhes da Transação")

valor_transacao = st.number_input("Valor da Transação (em dólares)", min_value=0, max_value=10000, value=50)
tempo_conta = st.number_input("Tempo de Conta (em meses)", min_value=0, max_value=120, value=6)
num_transacoes_ult_30d = st.number_input("Número de Transações nos Últimos 30 dias", min_value=0, max_value=1000, value=3)

# Para simplificar, usamos um selectbox para país de origem
pais_origem_opcoes = {
    "Brasil": 0,
    "EUA": 1,
    "Outros": 2
}

pais_origem_escolhido = st.selectbox("País de Origem", list(pais_origem_opcoes.keys()))
pais_origem = pais_origem_opcoes[pais_origem_escolhido]

# 3. Botão de Predição
if st.button("Verificar se é Fraude"):
    # Constrói o array/reshape adequado para o modelo
    input_array = np.array([[valor_transacao, tempo_conta, num_transacoes_ult_30d, pais_origem]])

    # 4. Executa a predição
    pred = fraud_model.predict(input_array)
    proba = fraud_model.predict_proba(input_array)

    st.write("## Resultado da Análise:")
    if pred[0] == 1:
        st.error("Alerta: Transação com ALTO risco de fraude.")
    else:
        st.success("Transação aparentemente legítima.")

    # 5. Probabilidade de fraude (opcional)
    st.write(f"**Probabilidade de Não Fraude:** {proba[0][0]:.2f}")
    st.write(f"**Probabilidade de Fraude:** {proba[0][1]:.2f}")
else:
    st.write("Informe os detalhes e clique em 'Verificar se é Fraude'.")