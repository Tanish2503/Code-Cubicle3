import pyautogui
import time
import pyperclip
import openai
from openai.error import RateLimitError, OpenAIError

while True:
    a=pyautogui.position()
    print(a)


def move_and_click(x, y, delay=1):
    pyautogui.moveTo(x, y)
    time.sleep(delay)
    pyautogui.click()

def select_text(start_x, start_y, end_x, end_y):
    pyautogui.moveTo(start_x, start_y)
    time.sleep(1)
    pyautogui.mouseDown(button='left')
    time.sleep(0.5)
    pyautogui.moveTo(end_x, end_y, duration=2)
    time.sleep(0.5)
    pyautogui.mouseUp(button='left')
    time.sleep(1)


move_and_click(319, 0, 2)
move_and_click(55, 40, 1)
move_and_click(237, 1014, 1)

select_text(282,111,672, 931)