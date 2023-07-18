#!/usr/bin/python3
import pyautogui as pg
import sys
import time
pg.FAILSAFE = False


xCoordinate = int(sys.argv[1])
yCoordinate = int(sys.argv[2])

x, y = pg.position()

pg.click(xCoordinate, yCoordinate)
pg.click(button='right')
print(x,y)
del sys, pg, xCoordinate, yCoordinate
