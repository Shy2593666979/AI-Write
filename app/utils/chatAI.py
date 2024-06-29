import requests
import openai
from app.settings import setting



def chat_deepseek(prompt):
    client = openai.OpenAI(api_key=setting.API_KEY,base_url=setting.BASE_URL)
    
    response = client.chat.completions.create(
        model=setting.CONFIG_MODEL,
        messages=[{'role':"user",'content':prompt}]
    )

    return response.choices[0].message.content