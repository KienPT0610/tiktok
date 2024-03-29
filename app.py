import pyautogui as pag
import time

time.sleep(5)

while True:
    pag.keyDown('down')
    time.sleep(2)
    pag.doubleClick(532, 450)
    pag.click(1387, 169)
    time.sleep(30)
    