import gradio as gr
import openai

# Ustawienia API OpenAI
openai.api_key = "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" # zastąp wartość API_KEY swoim kluczem API OpenAI

# Ustawienia interfejsu Gradio
title = "OpenAI Chatbot"
description = "Witaj! Jestem chatbotem opartym na modelu GPT-3."
inputs = [gr.components.Textbox(label="Wpisz pytanie")]
outputs = [gr.components.Textbox(label="Odpowiedź")]

# Funkcja wykonująca żądanie do OpenAI API
def generate_response(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.9,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop="BOT"
    )
    print(response)
    return response.choices[0].text.strip()

# Uruchomienie interfejsu Gradio
gr.Interface(
    fn=generate_response,
    inputs=inputs,
    outputs=outputs,
    title=title,
    description=description,
    theme="default").launch()