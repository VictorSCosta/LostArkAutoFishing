import pyautogui
import time


def fish():
    print("LostArkAutoFishing STARTED, open the game and start fishing.")

    while 1:
        if pyautogui.locateOnScreen('exclamation_mark.png', confidence=0.8) is not None:
            print("Fish caught")
            pyautogui.press('e')

            time.sleep(7)

            print("Fishing started")
            pyautogui.press('e')

        time.sleep(0.2)


if __name__ == '__main__':
    fish()

