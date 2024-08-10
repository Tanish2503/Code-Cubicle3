import pyautogui
import time
import pyperclip
import openai
from openai.error import RateLimitError, OpenAIError

openai.api_key = "sk-proj-OsRZ8cOOn4mpHpASuyJDT3BlbkFJxOYaDIAmotYQTZrLijZH"
def is_last_message_from_sender(chat_history, sender_name="Saarthak"):
    messages = chat_history.strip().split("\n")
    if not messages:
        return False

    # Find the last non-empty message that contains a timestamp and sender
    for message in reversed(messages):
        if message.strip() and "]" in message:
            # Extract the part of the message after the timestamp
            message_content = message.split("] ", 1)[-1]
            # Check if the sender name is in the extracted message content
            if message_content.startswith(sender_name):
                return True
            return False
    return False



def move_and_click(x, y, delay=1):
    pyautogui.moveTo(x, y)
    time.sleep(delay)
    pyautogui.click()

# Function to select text in WhatsApp
def select_text(start_x, start_y, end_x, end_y):
    pyautogui.moveTo(start_x, start_y)
    time.sleep(1)
    pyautogui.mouseDown(button='left')
    time.sleep(0.5)
    pyautogui.moveTo(end_x, end_y, duration=2)
    time.sleep(0.5)
    pyautogui.mouseUp(button='left')
    time.sleep(1)

# Function to bring WhatsApp to focus (if it's minimized or behind other windows)
def focus_whatsapp():
    pyautogui.hotkey('command', 'tab')  # Switch application
    time.sleep(1)
    move_and_click(235, 1018, 1)  # Click on WhatsApp icon (adjust coordinates as needed)

# Hover at (319, 0) for 3 seconds
move_and_click(319, 0, 2)
move_and_click(55, 40, 1)

# Focus on WhatsApp
focus_whatsapp()

while True:
    # Adjust the coordinates based on your screen resolution and WhatsApp window position
    select_text(557,189,784,1041)

    # Select the text and copy to clipboard
    pyautogui.hotkey('command', 'c')
    time.sleep(1)
    
    # Deselect the selected text
    pyautogui.click(670,702)

    chat_history = pyperclip.paste()
    print(chat_history)

    if is_last_message_from_sender(chat_history):
        try:
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": """
You are an automatic reply bot for Tanish, an 18-year-old Indian boy. Your job is to reply to his WhatsApp messages in a friendly, engaging, and contextually appropriate manner. Maintain a casual, polite tone, and try to match Tanish's style of conversation. Here are some guidelines:
1. If the message is a greeting or casual conversation, respond warmly and ask how the person is doing.
2. If the message contains a question, provide a clear and helpful answer. If you're not sure, it's okay to admit that and suggest looking it up together later.
3. If the message is about making plans, confirm or suggest alternatives based on what seems appropriate.
4. Use emojis sparingly to convey emotions.
5. Keep responses concise and to the point, around 1-2 sentences.
6. If the message is personal or sensitive, respond with empathy and support.
7. If you don't understand the message, ask for clarification in a polite way.
8. Never disclose that you are an AI unless explicitly asked.
9. Dont reply to messages like this [14:10, 16/07/2024] Tanish😁 
10. Use Hinglish
"""},
                    {"role": "user", "content": chat_history}
                ],
                max_tokens=100
            )
            response = completion.choices[0].message.content
            pyperclip.copy(response)
        except RateLimitError as e:
            print(f"Rate limit exceeded: {e}")
            time.sleep(60)
        except OpenAIError as e:
            print(f"An error occurred: {e}")

    move_and_click(686, 1006)
    pyautogui.hotkey('command', 'v')
    pyautogui.press('enter')

    time.sleep(5)  # Add a short delay to avoid rapid execution loops



