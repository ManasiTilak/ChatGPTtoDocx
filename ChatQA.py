from openai import OpenAI
from dotenv import load_dotenv
import openai
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

try:
    # Create a chat completion
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant and a coding expert. You are very good at writing coding blogs."},
            {"role": "user", "content": "Capital of India?"}
        ]
    )
    
    # Print the response content
    print(response.choices[0].message.content)
except Exception as e:
    print(f"An error occurred: {e}")