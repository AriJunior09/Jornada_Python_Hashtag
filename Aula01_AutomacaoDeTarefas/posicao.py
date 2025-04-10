import pyautogui
import time

""" time.sleep(4)

print(pyautogui.position()) """

# abrir o navegador (chrome)
pyautogui.PAUSE = 0.8
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no link 
pyautogui.write("https://www.linkedin.com/in/arijunior09/")
pyautogui.press("enter")
time.sleep(6)

pyautogui.scroll(-10000) # Dar scroll

