import pyautogui
import os
import time
import tkinter

if os.path.exists("elenco.txt") == False:
    pyautogui.alert('''Prima di eseguire il programma creare nella stessa cartella\n
                    il file elenco.txt con le carte da utilizzare''')
elif pyautogui.confirm(text='''Per il momento Tfum funziona solo con\n una risoluzione di Hearthstone di 1920x1080 fullscreen''', title='Tfum', buttons=['Quella in uso.\n Posso usare il programma','Aspetterò una nuova versione'])=='Aspetterò una nuova versione':
    pass
else:
    f = open("elenco.txt","r") 
    a=f.readlines()
    for n in range(len(a)):
        pyautogui.moveTo(940, 980)
        pyautogui.typewrite("%s" % a[n])
        pyautogui.press('ENTER')
        pyautogui.moveTo(940, 980)
        pyautogui.moveTo(370, 300)
        pyautogui.click(2)
        time.sleep(.1)
        pyautogui.moveTo(940, 980)
        pyautogui.click()
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('BACKSPACE')
    pyautogui.alert('Mazzo finito, buon gioco!')
