import pyautogui
import time

time.sleep(3)
print(pyautogui.position())  # Mostra a posição do mouse na tela

pyautogui.PAUSE = 0.8
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter") 

pyautogui.write("https://www.arealme.com/click-speed-test/pt/")
pyautogui.press("enter") 
time.sleep(3)
pyautogui.click(x=696, y=734)
time.sleep(1)
pyautogui.click(x=705, y=363,clicks=1000)