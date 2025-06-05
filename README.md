# BlinkMailBot 

BlinkMailBot is a lightweight Python tool that notifies you on Telegram when you receive emails matching certain keywords. It checks your Gmail inbox every 30 seconds and forwards relevant messages to you. From getting 2FA codes on the fly, to having urgent work emails notifying you on your Telegram instantly, you take full control of what gets filtered and sent. 

## Why? For whom?
Emails are often delayed, buried, or missed in cluttered inboxes. BlinkMailBot solves this by surfacing only important messages directly to the platform you use most: Telegram. This improves response time and ensures critical messages never go unnoticed.
As someone who often forgets to check my inbox, I have a tendency to miss important emails despite being on my laptop often for work. This bot is limited in that it only works when your pc/laptop is running as it is hosted locally, but works perfectly for my workflows.
If you're someone like me, always on your laptop for work, and highly active on telegram, but don't check your inbox often, or get drowned in spammy, unimportant nonsense, I hope you'll extract some value from this lightweight utility I've built. 

- Get 2fa codes on the fly
- Be notified of hidden recurring transactions, or track billing expenses easily
- Receive notifications from urgent work matters


## 🔧 Tech Stack

- Python
- Gmail API via Google Cloud
- OAuth 2.0 authorization (Auto refresh tokens and local storage)
- Telegram Bot API

## 📌 Features

- Monitors your Gmail inbox for new messages
- Filters emails based on keywords in the sender, subject, or snippet (Not case sensitive!)
- Sends relevant email alerts to your Telegram via a bot
- Oauth 2.0 authorization with automatic token refresh
- Local token storage and filter data

## 📁 Project Structure

```
BlinkMail/
├── client_secret.json
├── google_apis.py
├── telegram_bot.py
├── main.py
└── token files/
```

## ✅ Setup Instructions 

### Prerequisites
- Python3.x installed
- Cloned or downloaded this repository into local project within VSCode, Pycharm, or environment of choice
- Set up a virtual environment by typing the following into your terminal:
  ```bash
   python -m venv venv
   source venv/bin/activate   or .\venv\Scripts\activate on Windows

### 1. Enable Gmail API, OAuth2.0 

- Visit: https://console.cloud.google.com/
- Create a new project (top-left button, to the left of search bar) and name it whatever you like, leaving organisation as none
- Enable Gmail API - searchbar at the top of google cloud console, search gmail, click gmail API, click enable
- Configure OAuth consent screen - click OAuth consent screen on left panel under APIs and services, click get started, fill in app name and your own email, set to external, set own email again
- Go to audience (left panel still), scroll down to test users, add user, add the email you would like to be tracked
- Go to overview (left panel), create OAuth client, select desktop app as application type, name it whatever you like, create, and download JSON
- Place the downloaded JSON file in your project root folder through your own file explorer or otherwise
- Rename the file client_secret.json in your project root (IMPORTANT)

### 2. Create Telegram Bot

- Message [@BotFather](https://t.me/BotFather)
- Use `/newbot` and follow the prompts
- Save the Bot Token
- Open a chat with your bot and /start. Leave the chat open, its needed for later steps
- Get your `chat_id` by visiting:
  ```
  https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates
  ```
- Replace <YOUR_BOT_TOKEN> with your actual token. Go back to your chat and send any message to the bot, before returning to the browser and refresh the page.
- Look for "chat":{"id":123456789,...} in the JSON response. This number is your chat ID.
- Save the bot token and chat_id in a .env file in your project root, they MUST be named TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID
- Do so by creating a new file and name it .env in the project root, and writing the following 2 lines in the file:
  - TELEGRAM_BOT_TOKEN=your_token_here
  - TELEGRAM_CHAT_ID=your_chat_id_here
- No quotation marks needed
  

### 3. Install Dependencies
- Install dependencies by typing the following into terminal:
```bash
pip install -r requirements.txt
```

### 4. Run the Bot

```bash
python main.py
```
Upon running main.py:
You'll be asked to log in to your Gmail account and allow read access. This is a one time setup, and after giving access you can close your browser and the bot will run automatically. 
After that, the bot starts checking for new emails every 30 seconds and sends matches to Telegram.
Tokens are refreshed automatically and stored locally once access is given the first time, meaning the only form of maintainence after this is running main.py and leaving your pc/laptop on in the background. 
You will be notified via telegram whenever an email matching filters is received while your pc is running the program. 


To terminate the program, just do ctrl + C in your terminal and it will end the polling

## ✍️ Filter Customization

Edit the `KEYWORDS` list in `main.py`:

```python
KEYWORDS = ['payment', 'urgent', '2fa', 'billing']
```

## 📎 Notes

- Only messages in the Inbox label are scanned
- Duplicate messages won't be re-sent thanks to caching in memory
- All credentials are stored locally in `token files/`

## 🚫 Limitations

- Single-user setup only
- Requires your device to be always on (unless you deploy it)
- Currently filters only detect keywords presence in sender, header, or snippets of email body

---

## 📜 License and Usage

This project is licensed under the [MIT License](LICENSE).

Feel free to use, modify, or extend BlinkMailBot for your own purposes, within the terms of the license.
