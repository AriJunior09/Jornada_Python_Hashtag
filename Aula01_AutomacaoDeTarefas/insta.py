import pyautogui
import time

pyautogui.PAUSE = 0.8
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter") 
time.sleep(1)           # Espera 1 segundos para o navegador abrir
pyautogui.write("https://www.instagram.com/arijunior09")
pyautogui.press("enter") # Abre o Instagram
time.sleep(5)
pyautogui.click(x=852, y=759) # Clica na posição (852, 759) da tela
time.sleep(2)
pyautogui.click(x=820, y=583)
