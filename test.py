#!/usr/bin/python3
import subprocess
import sys
import cv2
import numpy as np



xCoordinate = int(sys.argv[1])
yCoordinate = int(sys.argv[2])


def start_waydroid():
    subprocess.run(['waydroid', 'show-full-ui'])

def stop_waydroid():
    subprocess.run(['waydroid', 'stop'])

def install_app(apk_path):
    subprocess.run(['waydroid', 'install', apk_path])

def run_app(package_name):
    subprocess.run(['waydroid', 'run', package_name])
    
def click_screen(x, y):
    subprocess.run(['adb', 'shell', 'input', 'tap', str(x), str(y)])    
    
       

#start_waydroid();
#click_screen(xCoordinate,yCoordinate);






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

# Example usage
find_image_on_screen('test.png')
