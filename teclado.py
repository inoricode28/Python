import pyautogui as pg 
import time 

pg.hotkey("win","r")
pg.typewrite("https://www.youtube.com/watch?v=iOa7uE23qc4=7s\n")
time.sleep(2)
pg.typewrite("k")
pg.hotkey("win","r")
pg.typewrite("notepad\n")
time.sleep(1)
pg.typewrite("pude lograr escribir en el notas\n")
pg.sleep(3)
pg.typewrite("estoy trabajando con codigo python\n")
time.sleep(2)
pg.typewrite("Y aqui finaliza\n")
