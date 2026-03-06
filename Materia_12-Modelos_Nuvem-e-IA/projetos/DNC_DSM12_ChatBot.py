import gradio as gr
from transformers import pipeline
import os

# Definir diretório de cache fora do repositório
# Isso pode ser um caminho absoluto para um diretório fora do seu projeto
os.environ["TRANSFORMERS_CACHE"] = "./modelos_cache"
os.environ["HF_HOME"] = "./modelos_cache"

# Use the text-generation pipeline with the BlenderBot model
modelo = pipeline("text-generation", model="facebook/blenderbot-400M-distill")

def responder(mensagem):
    # The pipeline returns a list of dicts; we take the first result's "generated_text"
    result = modelo(mensagem, max_length=100)
    return result[0]["generated_text"]

iface = gr.Interface(fn=responder, inputs="text", outputs="text")
iface.launch()