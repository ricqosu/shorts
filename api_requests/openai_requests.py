# docs - https://platform.openai.com/docs/guides/gpt

import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.environ.get("OPEN_API_KEY")

def send_openai_request(prompt):
  print('Getting a story based off your prompt from ChatGPT...')
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    max_tokens=450,
    messages=[
        {
            "role": "system",
            "content": "You create entertaining, easy to read stories like the ones \
               you might find on Reddit in 250 words or less",
        },
        {"role": "user", "content": prompt},
    ],
  )
  story = response.choices[0].message.content.replace('\n\n', ' ')
  return story

