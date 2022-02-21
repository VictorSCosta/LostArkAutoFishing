import logging

import pyautogui
import time
import random
import constants
from utils import resource_path

total_fish_caught = 0
exclamation_mark_img = resource_path('img/exclamation_mark.png')
throw_bait_img = resource_path('img/throw_bait.png')


def is_on_screen(img):
    return pyautogui.locateOnScreen(img, confidence=0.7) is not None


def fish(buffs_enabled=True):
    print("LostArkAutoFishing STARTED, open the game and start fishing.")

    while 1:
        if is_on_screen(exclamation_mark_img):
            pyautogui.press(constants.FLOAT_FISHING)
            print("Fish caught")
            delay = random.randint (670,720)/100
            print("Waiting for " + str(delay) + " seconds")
            time.sleep(delay)

            if buffs_enabled:
                throw_bait()

            print("Fishing started")
            pyautogui.press(constants.FLOAT_FISHING)

        time.sleep(0.2)


def throw_bait():
    if is_on_screen(throw_bait_img):
        print("Threw bait")
        pyautogui.press(constants.THROW_BAIT)
        time.sleep(5)


if __name__ == '__main__':
    fish()
