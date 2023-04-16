import os
from dotenv import load_dotenv
import openai


load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')
model = openai.Model.retrieve("text-davinci-003")
print(model)