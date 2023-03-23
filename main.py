import tkinter as tk
import requests as r
import time
from dotenv import load_dotenv
import os

load_dotenv()

def getWeather(canvas):
    city = textField.get()
    api_key = os.environ.get('API_KEY')
    api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    json_data = r.get(api).json()
    localidad = json_data['name'] + '-' + json_data['sys']['country']
    timezone_api = api
    timezone_data = r.get(timezone_api).json()
    timezone_offset = timezone_data['timezone']  # Obtener el offset de la zona horaria en segundos
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp']-273.15)
    min_temp = int(json_data['main']['temp_min']-273.15)
    max_temp = int(json_data['main']['temp_max']-273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))
    current_time_utc = time.gmtime()  # Obtener la hora UTC actual
    current_time_local = time.localtime(
    time.mktime(current_time_utc) + timezone_offset)  # Convertir a la hora local de la ciudad
    current_time_formatted = time.strftime('%I:%M %p', current_time_local)  # Formatear la hora local

    final_info = condition + "\n" + str(temp) + "°c"
    final_data = "\n" + "Localidad: " + str(localidad) + "\n" + "Minima: " + str(min_temp) + "°C" + "\n" + "Maxima: " + str(max_temp) + "°C" +"\n" + "Presion: " + str(pressure) + "\n" +"Humedad: " + str(humidity) + "\n" + "Hora: " + current_time_formatted
    label1.config(text = final_info)
    label2.config(text = final_data)

canvas = tk.Tk()
canvas.geometry("900x800")
canvas.title("Weather App")
canvas.configure(bg='#49A')
f = ('poppins', 15)
t = ('poppins', 20)

textField = tk.Entry(canvas, width=30, font=f)
textField.pack(pady = 10)
textField.focus()
textField.bind('<Return>', getWeather)

label1 = tk.Label(canvas, text="", font=t, bg='#49A')
label1.pack()
label2 = tk.Label(canvas, text="", font=t, bg='#49A')
label2.pack()
canvas.mainloop()