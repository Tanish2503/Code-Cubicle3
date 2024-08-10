import time
import openai
from openai.error import RateLimitError, OpenAIError

openai.api_key = "sk-proj-OsRZ8cOOn4mpHpASuyJDT3BlbkFJxOYaDIAmotYQTZrLijZH"

def create_completion():
    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a virtual assistant named Jarvis, skilled in general tasks performed by Alexa and Google Cloud."},
                {"role": "user", "content": "What is programming?"}
            ],
            max_tokens=100
        )
        print(completion.choices[0].message['content'])
    except RateLimitError as e:
        print(f"Rate limit exceeded: {e}")
        time.sleep(60)  # Wait for 60 seconds before retrying
        create_completion()
    except OpenAIError as e:
        print(f"An error occurred: {e}")

create_completion()
