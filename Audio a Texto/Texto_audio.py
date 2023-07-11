import pyttsx3
from IPython.display import Audio
import openai

openai.api_key = "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"

idioma_audio = "Castellano" # Idioma del audio
idioma_traducir = "Ingles" # Idioma a traducir

# Pasamos el audio a texto
audio_file = open("prueba.mp3","rb")
transcript = openai.Audio.transcribe("whisper-1",audio_file)

texto = 'Eres un traductor del '+idioma_audio+' al '+idioma_traducir
traduccion = "traduceme el siguiente texto "+transcript["text"]

# Traduccion de ChatGPT

messages = [{"role":"system", "content": texto}]
messages.append({"role":"user", "content": traduccion})
response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
respuesta = "El texto a traducir es: "+transcript["text"]+"\n\n" + "y la traducion de ChatGPT es:"+ "\n\n" + response["choices"][0]["message"]["content"]
print(respuesta)

# A partir de esa respuesta creamos un audio con una voz

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[2].id)

engine.say(response["choices"][0]["message"]["content"])
engine.runAndWait()

engine.save_to_file(response["choices"][0]["message"]["content"], "bot_message.mp3")
engine.runAndWait()

Audio("bot_message.mp3", autoplay=True)