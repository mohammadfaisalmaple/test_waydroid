#!/usr/bin/python3
import os
import datetime
import pyautogui as pg
import time
import sys
import subprocess
import cv2
import numpy as np

pg.FAILSAFE = False
searchImage = sys.argv[1]
timeOut = int(sys.argv[2])
start_time = time.time()
dir_path = os.path.dirname(os.path.realpath(__file__))
date = datetime.datetime.now().strftime("%Y-%m-%d")


def prepareLogsFolder():
    userName = os.environ.get('USER')
    if (not (os.path.isdir("/home/"+userName + "/pythonLogs"))):
        os.mkdir("/home/"+userName + "/pythonLogs")


prepareLogsFolder()
userName = os.environ.get('USER')
logFileLocation = "/home/"+userName + \
    "/pythonLogs/" + '/' + str(date) + ".txt"

logsWritingObject = open(logFileLocation, "a")
logsWritingObject.write("SCRIPT : " + os.path.basename(__file__) + "\n")
logsWritingObject.write("TARGET : " + os.path.basename(searchImage) + "\n")
logsWritingObject.write("TIME OUT  : " + str(timeOut) + "\n")
logsWritingObject.write("START @ " + str(datetime.datetime.now()) + "\n")



def find_image_on_screen(template_path):
    # Capture a screenshot of the Waydroid screen using adb
    subprocess.run(['adb', 'shell', 'screencap', '-p', '/sdcard/screenshot.png'])
    subprocess.run(['adb', 'pull', '/sdcard/screenshot.png'])

    # Load the template image
    template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)

    # Load the screenshot image
    screenshot = cv2.imread('screenshot.png', cv2.IMREAD_GRAYSCALE)

    # Perform template matching
    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)

    # Set a threshold for the match
    threshold = 0.8
    loc = np.where(result >= threshold)

    if len(loc[0]) > 0:
        # Click on the center of the matched image
        h, w = template.shape
        x = loc[1][0] + w // 2
        y = loc[0][0] + h // 2
        click_screen(x, y)
   
def click_screen(x, y):
    subprocess.run(['adb', 'shell', 'input', 'tap', str(x), str(y)])
   
  
find_image_on_screen(searchImage)


logsWritingObject.write("END " + str(datetime.datetime.now()) + "\n")
logsWritingObject.write("TOTAL TIME  " + str(time.time() - start_time) + "\n")

