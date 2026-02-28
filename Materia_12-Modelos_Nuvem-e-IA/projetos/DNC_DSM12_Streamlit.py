import streamlit as st
import numpy as np

# Exemplo: Suponha que temos um modelo de IA previamente treinado
# Para fins de ilustração, vamos simular um modelo de classificação simples
# que classifica algo em 2 categorias (0 ou 1).
def fake_model_predict(features):
    """
    Esta função simula uma predição de um modelo real.
    Suponha que 'features' é uma lista ou array de valores numéricos.
    """
    # Exemplo simplificado: Se a soma dos recursos for maior que 10, retorna 1, caso contrário 0.
    if sum(features) > 10:
        return 1
    else:
        return 0

# Título do aplicativo
st.title("Interface Simples para um Modelo de IA")

# Descrição inicial
st.write("Este aplicativo demonstra como interagir com um modelo de IA via Streamlit.")

# Seção de inputs
st.header("Entrada de Dados")

# Exemplo de sliders para capturar variáveis (simulando features de um dataset, como idade, renda, etc.)
var1 = st.slider("Variável 1 (Ex.: Idade)", 0, 100, 25)
var2 = st.slider("Variável 2 (Ex.: Renda em milhares)", 0, 50, 10)
var3 = st.slider("Variável 3 (Ex.: Pontos de Crédito)", 0, 100, 50)

# Botão para realizar a predição
if st.button("Fazer Predição"):
    # Constrói um array ou lista com os inputs
    features = [var1, var2, var3]
    prediction = fake_model_predict(features)

    st.write("## Resultado da Predição:")
    if prediction == 1:
        st.success("O modelo previu a categoria '1'!")
    else:
        st.warning("O modelo previu a categoria '0'.")
else:
    st.write("Clique em 'Fazer Predição' para ver o resultado do modelo.")