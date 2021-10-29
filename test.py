import time
import pyautogui
import cv2
import mss
import numpy as np
import keyboard
#first needle 

pyautogui.PAUSE = 0.0

needle = cv2.imread("needle.png", cv2.IMREAD_UNCHANGED)

w = needle.shape[1]
h = needle.shape[0]


#second needle

needle2 = cv2.imread("needle2.png", cv2.IMREAD_UNCHANGED)

w2 = needle2.shape[1]
h2 = needle2.shape[0]


#third needle

needle3 = cv2.imread("needle3.png", cv2.IMREAD_UNCHANGED)

w3 = needle3.shape[1]
h3 = needle3.shape[0]

#fourth needle

needle4 = cv2.imread("needle4.png", cv2.IMREAD_UNCHANGED)

w4 = needle4.shape[1]
h4 = needle4.shape[0]

threshold = .80

left = {"top": 600, "left": 270, "width": 160, "height": 135}
right = {"top": 600, "left": 430, "width": 160, "height": 135}

show_left = True

while True:
    scr = mss.mss()
    if show_left == True:
        scr = np.array(scr.grab(left))
        result = cv2.matchTemplate(scr, needle, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        result2 = cv2.matchTemplate(scr, needle2, cv2.TM_CCOEFF_NORMED)
        min_val2, max_val2, min_loc2, max_loc2 = cv2.minMaxLoc(result2)
        scr = scr.copy()
        if max_val >= threshold or max_val2 >= threshold:
            pyautogui.click(514, 693)
            pyautogui.click(514, 693)
            show_left = False
        else:
            pyautogui.click(350, 696)



    elif show_left == False:
        scr = np.array(scr.grab(right))
        result3 = cv2.matchTemplate(scr, needle3, cv2.TM_CCOEFF_NORMED)
        min_val3, max_val3, min_loc3, max_loc3 = cv2.minMaxLoc(result3)
        result4 = cv2.matchTemplate(scr, needle4, cv2.TM_CCOEFF_NORMED)
        min_val4, max_val4, min_loc4, max_loc4 = cv2.minMaxLoc(result4)
        scr = scr.copy()
        if max_val3 >= threshold or max_val4 >= threshold:
            pyautogui.click(350, 696)
            pyautogui.click(350, 696)
            show_left = True
        else:
            pyautogui.click(514, 693)
        
    cv2.imshow('Screen Shot', scr)
    cv2.waitKey(1)
    if keyboard.is_pressed('q'):
        break


