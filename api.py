import os
from dotenv import load_dotenv
import openai

load_dotenv()

prompt = input('Enter prompt here:\n')
openai.api_key = os.getenv('OPENAI_API_KEY')
res = openai.Image.create(
    prompt=prompt,
    n=1,
    size='1024x1024'
)

url = res['data'][0]['url']

print(url)
