import gradio as gr
from transformers import pipeline

# Use the text2text-generation pipeline with the BlenderBot model
modelo = pipeline("text2text-generation", model="facebook/blenderbot-400M-distill")

def responder(mensagem):
    # The pipeline returns a list of dicts; we take the first result's "generated_text"
    result = modelo(mensagem, max_length=100)
    return result[0]["generated_text"]

iface = gr.Interface(fn=responder, inputs="text", outputs="text")
iface.launch()
