
# Asistente virtual
# Importamos las librerias necesarias

import pyttsx3
import speech_recognition as sr
from datetime import datetime

# --- Definiciones de funciones auxiliares ---
# ¡IMPORTANTE! Las funciones deben definirse antes de ser llamadas.

def obtener_nombre_mes(numero_mes):
    nombres_meses = {
        1: "enero", 2: "febrero", 3: "marzo", 4: "abril",
        5: "mayo", 6: "junio", 7: "julio", 8: "agosto",
        9: "septiembre", 10: "octubre", 11: "noviembre", 12: "diciembre"
    }
    return nombres_meses.get(numero_mes, "desconocido")

# --- Bloque 1: Configuración del reconocimiento de voz y escucha ---

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Di algo:")
    # Opcional: Ajustar el umbral de ruido para mejorar el reconocimiento
    # r.pause_threshold = 1
    # r.adjust_for_ambient_noise(source, duration=1)
    audio = r.listen(source)

try:
    texto = r.recognize_google(audio, language="es-Es")
    print("Dijiste:", texto)
    texto = texto.lower() # Convertir a minúsculas para facilitar el procesamiento
except sr.UnknownValueError:
    print("No pude entender lo que dijiste.")
    texto = ""
except sr.RequestError as e:
    print(f"Error al conectar con el servicio de Google: {e}")
    texto = ""

# --- Bloque 2: Configuración del asistente de voz (pyttsx3) ---

engine = pyttsx3.init()
# Opcional: Configuración de la voz
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)

# El asistente saluda al inicio
engine.say("Hola, ¿En qué puedo ayudarte?")
engine.runAndWait()

# --- Bloque 3: Procesamiento de comandos y respuestas ---

# Programamos respuestas rapidas
if "hora" in texto:
    hora = datetime.now().strftime("%H:%M")
    engine.say(f"La hora es {hora}")
    engine.runAndWait()

elif "cómo estás" in texto:
    engine.say("Estoy aprendiendo contigo")
    engine.runAndWait()

# --- Función: QUÉ DÍA ES HOY ---
elif "qué día es hoy" in texto or "qué día estamos" in texto or "dime el día" in texto:
    hoy = datetime.now()
    dias_semana = {
        0: "lunes", 1: "martes", 2: "miércoles", 3: "jueves",
        4: "viernes", 5: "sábado", 6: "domingo"
    }
    nombre_dia = dias_semana[hoy.weekday()]

    # Aquí se llama a obtener_nombre_mes, y ahora ya estará definida
    fecha_formateada = hoy.strftime(f"%d de {obtener_nombre_mes(hoy.month)} de %Y")

    engine.say(f"Hoy es {nombre_dia}, {fecha_formateada}.")
    engine.runAndWait()

else:
    engine.say("No entendí eso")
    engine.runAndWait()
