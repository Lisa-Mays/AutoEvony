import subprocess
import cv2
import numpy as np
import os
import time as tm

class Auto:
    def __init__(self, ip='127.0.0.1', port=''):
        self.ip = ip
        self.port = port
        self.pwd = 'cd android'
        # Connect to the device
        subprocess.run(f'{self.pwd} && adb connect {self.ip}:{self.port}', shell=True)

    def screen_capture(self):
        # Capture the screen
        pipe = subprocess.Popen(f'{self.pwd} && adb -s {self.ip}:{self.port} exec-out screencap -p',
                                stdout=subprocess.PIPE, shell=True)
        image_bytes = pipe.stdout.read()
        image = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), cv2.IMREAD_COLOR)
        return image
    
    def find_img(self, img,screenshot, threshold=0.9, num_positions=1):
        if os.path.exists(img):
            template = cv2.imread(img)
            result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
            loc = np.where(result >= threshold)
            positions = list(zip(*loc[::-1]))[:num_positions]
            if not positions:
                return False
            return positions
        else:
            return False
    
    def click(self, x, y):
        os.system(f"{self.pwd} && adb -s {self.ip}:{self.port} shell input tap {x} {y}")
        
    def swipe(self, x1, y1, x2, y2, duration=1000):
        os.system(f"{self.pwd} && adb -s {self.ip}:{self.port} shell input swipe {x1} {y1} {x2} {y2} {duration}")
        os.system(f"{self.pwd} && adb -s {self.ip}:{self.port} shell input swipe 360 650 0 650 600")
    
    def esc(self):
        os.system(f"{self.pwd} && adb -s {self.ip}:{self.port} shell input keyevent 111")

