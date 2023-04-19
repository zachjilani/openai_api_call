import os
from dotenv import load_dotenv
import openai

prompt = 'a white cat'
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')
model = openai.Model.retrieve("text-davinci-003")
print(model)
res = openai.Image.create(
    prompt=prompt,
    n=1,
    size='1024x1024'
)

url = res['data'][0]['url']

print(url)