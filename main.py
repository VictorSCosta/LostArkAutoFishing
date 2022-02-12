import pyautogui
import time


def fish():
    while 1:
        if pyautogui.locateOnScreen('exclamation_mark.png', confidence=0.8) is not None:
            print("ACHEI")
            pyautogui.press('e')

            time.sleep(7)

            print("Pescando novamente")
            pyautogui.press('e')

        time.sleep(0.2)


if __name__ == '__main__':
    fish()

