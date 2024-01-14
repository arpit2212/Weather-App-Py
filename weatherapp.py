import tkinter as tk
import requests
import time


 
api_key = "a9173790278131156fc3a41c215b85e8"
def getWeather():

    city = textField.get()
    apiUrl = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    
    result = requests.get(apiUrl)
    data = result.json()
    # condition = data['weather'][0]['main']
    temp = int(data['main']['temp'] - 273.15)
    min_temp = int(data['main']['temp_min'] - 273.15)
    max_temp = int(data['main']['temp_max'] - 273.15)
    pressure = data['main']['pressure']
    humidity = data['main']['humidity']
    wind = data['wind']['speed']

    # final_info = condition + "\n" + str(temp) + "°C" 
    final_data = "\n"+ "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(max_temp) + "°C" +"\n" + "Pressure: " + str(pressure) + "\n" +"Humidity: " + str(humidity) + "\n" +"Wind Speed: " + str(wind)
    # label1.config(text = final_info)
    label2.config(text = final_data)


canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")
smallText = ("poppins", 15, "bold")
largeText = ("poppins", 35, "bold")

textField = tk.Entry(canvas, justify='center', width = 20, font = largeText)
submitButton = tk.Button(canvas, text="Get Result", command=getWeather)
textField.pack(pady = 20)
submitButton.pack(pady = 15)

textField.focus()

label1 = tk.Label(canvas, font=largeText)
label1.pack()
label2 = tk.Label(canvas, font=smallText)
label2.pack()
canvas.mainloop()