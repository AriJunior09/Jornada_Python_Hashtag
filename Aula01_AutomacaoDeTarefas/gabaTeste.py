# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa 
# https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import time

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas
pyautogui.PAUSE = 0.8

# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no link 
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)


# Passo 2: Fazer login
# selecionar o campo de email
pyautogui.click(x=802, y=406)
# escrever o seu email
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab") # passando pro próximo campo
pyautogui.write("1234")
pyautogui.click(x=920, y=575) # clique no botao de login
time.sleep(3)

codigo = "7894900231456"
pyautogui.write(codigo)
pyautogui.press("tab")

marca = "Ferrari"
pyautogui.write(marca)
pyautogui.press("tab")

tipo = "Esportivo"
pyautogui.write(tipo)
pyautogui.press("tab")

categoria = "importado"
pyautogui.write(categoria)
pyautogui.press("tab")
pyautogui.write("S")
pyautogui.press("tab")
pyautogui.write("R$ 3.190.000,00")
pyautogui.press("tab")
pyautogui.write("R$ 1.800.000,00")
pyautogui.press("tab")
pyautogui.write("Novo")
pyautogui.press("tab")

pyautogui.press("enter") # clicar no botao de enviar
   # dar scroll de tudo pra cima
pyautogui.scroll(5000)