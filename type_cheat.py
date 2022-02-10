#!python3
import time as t
try:
    import pyautogui as pag
except ImportError:
    import os
    os.system("python -m pip install pyautogui")
    import pyautogui as pag
now=' '
word=''
while now!='':
    now=input()
    word=word+' '+now
t.sleep(3)
pag.typewrite(word)
