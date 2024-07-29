# importando biblioteca para ajudar a desenvolver o código.

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
import ttkbootstrap as ttk

# função para pegar as informações de clima da OpenWeatherMap API.
def get_weather(city):
    API_key = "270eaa26a11169c2b29550644f770fe4"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
    res = requests.get(url)

    if res.status_code == 404:
        messagebox.showerror("Erro", "Cidade não Encontrada")
        return None

    weather = res.json()  # Transforma a resposta do site em um formato organizado de dados
    icon_id = weather['weather'][0]['icon']  # Pega o ícone que mostra o tipo de clima (sol, chuva, etc.)
    temperature = weather['main']['temp'] - 273.15  # Converte a temperatura de Kelvin para Celsius
    description = weather['weather'][0]['description']  # Guarda todas as informações do clima
    city = weather['name']  # Pega o nome da cidade das informações do clima
    country = weather['sys']['country']  # Pega o código do país das informações do clima

    # Agora vamos importar o ícone de clima
    icon_url = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
    return icon_url, temperature, description, city, country

# função de busca
def search():
    city = city_entry.get()
    result = get_weather(city)
    if result is None:
        return
    # Se a cidade for encontrada, mostrar as informações.
    icon_url, temperature, description, city, country = result
    location_label.configure(text=f"{city}, {country}")
   
    # pega o ícone de clima na URL e aplica no icon_label
    image = Image.open(requests.get(icon_url, stream=True).raw)
    icon = ImageTk.PhotoImage(image)
    icon_label.configure(image=icon)
    icon_label.image = icon

    # atualiza o temperature_label e description_label
    temperature_label.configure(text=f"Temperatura: {temperature:.2f}°C")
    description_label.configure(text=f"Descrição: {description}")

# inicializando a janela principal
root = ttk.Window(themename="morph")
root.title("Previsão Certa")
root.geometry("400x400")

# adicionando entry widget para entrada da cidade
city_entry = ttk.Entry(root, font="Helvetica, 18")
city_entry.pack(pady=10)

# adicionando o botão de busca
search_button = ttk.Button(root, text="Search", command=search, bootstyle="warning")
search_button.pack(pady=10)

# label(rótulo/widget) para mostrar o nome do local (cidade/país)
location_label = tk.Label(root, font="Helvetica, 25")
location_label.pack(pady=20)

# adicionando o ícone do clima
icon_label = tk.Label(root)
icon_label.pack()

# adicionando o widget de temperatura
temperature_label = tk.Label(root, font="Helvetica, 20")
temperature_label.pack()

# adicionando o widget de descrição
description_label = tk.Label(root, font="Helvetica, 20")
description_label.pack()

# executando a aplicação
root.mainloop()
