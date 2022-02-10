import time as t
import pyautogui as pag
now=' '
word=''
while now!='':
    now=input()
    word=word+' '+now
t.sleep(3)
pag.typewrite(word)
