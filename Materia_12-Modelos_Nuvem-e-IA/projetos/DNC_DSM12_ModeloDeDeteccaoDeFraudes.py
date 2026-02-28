import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle

# Exemplo de dados de transações simuladas.
# Variáveis que podem influenciar fraude:
#  - valor_transacao (em dólares)
#  - tempo_conta (em meses desde criação da conta do usuário)
#  - num_transacoes_ult_30d (quantidade de compras feitas nos últimos 30 dias)
#  - pais_origem (codificado numericamente, ex.: 0 = Brasil, 1 = EUA, 2 = Outros)
# Alvo (fraude): 1 = fraude, 0 = legítimo

data = {
    'valor_transacao':            [15, 200, 3500, 60, 500, 9000, 30, 850, 4999],
    'tempo_conta':                [2,  24,  1,   12, 36,  0,    6,  48,  3],
    'num_transacoes_ult_30d':     [1,   5,   0,   3,  10,  20,   2,  15,  4],
    'pais_origem':                [0,   0,   2,   2,  1,   1,    0,  1,   2],
    'fraude':                     [0,   0,   1,   0,  0,   1,    0,  0,   1]
}

df = pd.DataFrame(data)

X = df[['valor_transacao', 'tempo_conta', 'num_transacoes_ult_30d', 'pais_origem']]
y = df['fraude']

# Treina um modelo de Regressão Logística simples
model = LogisticRegression()
model.fit(X, y)

# Salva o modelo em um arquivo .pkl
with open('modelo_fraude.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Modelo de fraude treinado e salvo em 'modelo_fraude.pkl'")