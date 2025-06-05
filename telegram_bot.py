import requests
import os
from dotenv import load_dotenv

load_dotenv() 
# Replace with your actual Bot Token and your Chat ID
BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

def send_telegram_message(text):
    #debug statement
    print('function to send msg called')
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    payload = {'chat_id': CHAT_ID, 'text': text}
    response = requests.post(url, data=payload)


    #debug statements
    print(f"Status Code: {response.status_code}")
  