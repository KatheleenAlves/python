import pyautogui 
import pandas as pd
import pyperclip
import time

bancodedados = pd.read_excel(r"C:\Users\A440975\Downloads\LabTorque\pythonautomate\database.xlsx")

pyautogui.PAUSE = 0.3
pyautogui.hotkey('alt','tab') 
pyautogui.hotkey('ctrl','shift','f')
pyautogui.hotkey('ctrl','a')            
pyautogui.hotkey('del')
pyperclip.copy('Apontamento de Horas por Funcionário')
pyautogui.hotkey('ctrl','v')
pyautogui.press('enter', presses=2)
time.sleep(2)

for linha in bancodedados.index:

    tb = bancodedados.loc[linha, "TB"]

    pyautogui.press('f3')

    time.sleep(1.5)
    pyautogui.write(str(tb))
    pyautogui.press('enter')
    time.sleep(1.5)
    pyautogui.press('tab')
    pyautogui.press('f5')

    dwo = bancodedados.loc[linha, "DWO"]
    pyautogui.write(str(dwo))
    pyautogui.press('tab', presses=2)
    time.sleep(3)
    tempo = bancodedados.loc[linha, "Tempo"]
    pyautogui.write(str(tempo/60).replace('.',','))
    pyautogui.sleep(2)  
    pyautogui.press('f12')
    pyautogui.press('f5')
    time.sleep(1.5)
    pyautogui.press('f12')


    
    

