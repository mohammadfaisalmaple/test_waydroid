#!/usr/bin/python3
import subprocess
import sys

apk_path = str(sys.argv[1])


def install_app(apk_path):
    subprocess.run(['adb', 'install', apk_path])
    
install_app(apk_path)    
  
    
