import pyautogui
import time


def repeat_action():
    # Wait for the application window to appear
    time.sleep(3)
    print("Running")

    # Perform the action in a loop
    for _ in range(1000):  # Repeat the action 5 times
        # Move the mouse to a specific position
        #Select student
        x = 259
        y = 114
        pyautogui.moveTo(x, y, duration=0.5)  # Change the
        # coordinates as per your requirement
        # Click at the current mouse position
        pyautogui.click()
        pyautogui.rightClick()

        #Click cancel transaction
        x = 330
        y = 141
        pyautogui.moveTo(x, y, duration=0.5)  # Change the coordinates as per your requirement
        # Click at the current mouse position
        pyautogui.click()

        #Click yes to confirm cancel
        x = 732
        y = 436
        pyautogui.moveTo(x, y, duration=0.5)  # Change the coordinates as per your requirement
        # Click at the current mouse position
        pyautogui.click()


        # Wait for a brief moment before repeating the action
        time.sleep(5)

print(pyautogui.size())
time.sleep(5)
print(print(pyautogui.position()))
repeat_action()