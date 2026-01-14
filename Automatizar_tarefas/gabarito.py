import pyautogui
import time 

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# abrir windows, clicar na barra de pesquisa, digitar edje, clicar enter, clicar na barra de pesquisa do edge, clicar na barra de pesquisa, digitar link, clicar enter

pyautogui.press('win')
time.sleep(1)
pyautogui.write('edge')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
pyautogui.click(x=100, y=100)  # Click on the search bar in Edge
time.sleep(1)
pyautogui.write(link)
time.sleep(1)
pyautogui.press('enter')
time.sleep(3)

# clicar em email, digitar email, clicar em senha, digitar senha, clicar em entrar

pyautogui.click(x=601, y=397)
time.sleep(1)
pyautogui.write("izadorainteligente@gmail.com")
time.sleep(1)
pyautogui.press('tab')
pyautogui.write("jesusefiel1234@")
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(5)

# importar base de dasos

import pandas as pd
tabela = pd.read_csv("produtos.csv")
print (tabela)

# configurar etapas da tarefa
for linha in tabela.index:


