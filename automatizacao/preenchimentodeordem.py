import pyautogui
import pandas as pd
import time

import pyperclip
import clipboard

pyautogui.PAUSE = 0.3   

pyautogui.alert(text="Bem-Vindo, Manutentor ! \n Você está pronto?", button='OK', title='ALERTA VOLVO')

time.sleep(3)

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(1)
pyautogui.hotkey("win","Up")

pyautogui.write("https://forms.gle/woczdxzuQb7g1CnU9")
pyautogui.press("enter")
time.sleep(2)

tabela = pd.read_excel(r"C:\Users\karin\Downloads\BancodeDadosOrdensdeServico.xlsx")

for linha in tabela.index:
    pyautogui.click(x=603, y=706)

    ordem = tabela.loc[linha, "Numero Ordem"]
    pyautogui.write(str(ordem))
    pyautogui.press("tab")
    
    diretriz = tabela.loc[linha, "Diretriz"]
    pyautogui.write(str(diretriz))
    pyautogui.press("tab")

    descfalha = tabela.loc[linha, "Descrição da Falha"]
    pyautogui.write(str(descfalha))
    pyautogui.press("tab")

    responsavel = tabela.loc[linha, "Responsável pela Execução"]
    pyautogui.write(str(responsavel))
    pyautogui.press("tab")

    org = tabela.loc[linha, "Organização de Manutenção"]
    pyautogui.write(str(org))
    pyautogui.press("tab")

    data = tabela.loc[linha, "Data"]
    pyautogui.write(str(data))
    pyautogui.press("tab")
    
    pyautogui.press("enter")
    time.sleep(2)
    
    pyautogui.press("f5")

    time.sleep(2)

    #pyautogui.scroll(5000)  