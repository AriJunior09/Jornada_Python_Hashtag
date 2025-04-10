import pyautogui
import time


# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.press -> apertar 1 tecla
# pyautogui.write -> escrever um texto
# pyautogui.hotkey -> combinação de teclas
# pyautogui.PAUSE = 0.3

pyautogui.PAUSE = 0.8  # Tempo de espera entre os comandos
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")                           # abrir o navegador (chrome)

pyautogui.write("https://github.com/AriJunior09")  # abrir o GitHub
pyautogui.press("enter")
time.sleep(3)

pyautogui.hotkey("ctrl", "t")
pyautogui.write("https://www.linkedin.com/in/arijunior09/") # abrir o LinkedIn
pyautogui.press("enter")
time.sleep(5)

pyautogui.hotkey("ctrl", "t")
pyautogui.write("https://www.instagram.com/arijunior09") # abrir o Instagram
pyautogui.press("enter")

