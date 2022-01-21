# Minha primeira Api

# Importando as bibliotecas

import tkinter as tk
import requests
import time

def pega_clima(janela):
    cidade = entry_descricao.get()
    api = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid=fc5916a4484d90f21e9cd3016adbc390"

    dados_json = requests.get(api).json()
    condicao = dados_json['weather'][0]['main']
    temperatura = int(dados_json['main']['temp'] - 273.15) # Convertendo a temperatura de °K p/ °C
    temperatura_minima = int(dados_json['main']['temp_min'] - 273.15)
    temperatura_maxima = int(dados_json['main']['temp_max'] - 273.15)
    umidade = dados_json['main']['humidity']
    vento = dados_json['wind']['speed'] * (3.6) # Converte p/ km/h
    nascer_do_sol = time.strftime('%I:%M:%S', time.gmtime(dados_json['sys']['sunrise'] - 10800))
    por_do_sol = time.strftime('%I:%M:%S', time.gmtime(dados_json['sys']['sunset'] - 10800))

    info_final = f"{condicao}\n {str(temperatura)} °c"
    dados_finais = f"""\nTemperatura Máxima: {str(temperatura_maxima)}ºC\nTemperatura Mínima: {str(temperatura_minima)}ºC
                   \nUmidade: {umidade}%\nVelocidade do vento: {vento:.1f} Km/h\nNascer do Sol: {nascer_do_sol}\nPôr do Sol: {por_do_sol}"""
    label1.config(text=info_final)
    label2.config(text=dados_finais)


janela = tk.Tk()
janela.geometry('600x500')
janela.title("Minha Api de Clima")
primeira_fonte = ("poppins", 15, "bold")
segunda_fonte = ("poppins", 35, "bold")


entry_descricao = tk.Entry(janela, justify='center', width=20,  font=primeira_fonte)
entry_descricao.pack(pady=20)
entry_descricao.focus()
entry_descricao.bind('<Return>', pega_clima)

label1 = tk.Label(janela, font=segunda_fonte)
label1.pack()
label2 = tk.Label(janela, font=primeira_fonte)
label2.pack()

janela.mainloop()