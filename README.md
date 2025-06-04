# BlinkMailBot 

BlinkMailBot is a lightweight Python tool that notifies you on Telegram when you receive emails matching certain keywords. It checks your Gmail inbox every 30 seconds and forwards relevant messages to you.

# Why?
Emails are often delayed, buried, or missed in cluttered inboxes. BlinkMailBot solves this by surfacing only important messages directly to the platform you use most: Telegram. This improves response time and ensures critical messages never go unnoticed.


## 🔧 Tech Stack

- Python
- Gmail API via Google Cloud
- OAuth 2.0 authorization
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
- Forked and pulled this repository into local project within VSCode, Pycharm, or environment of choice

### 1. Enable Gmail API, OAuth2.0 

- Visit: https://console.cloud.google.com/
- Create a new project (name it whatever you like)
- Enable Gmail API
- Configure OAuth consent screen (internal for personal use)
- Leave scope as empty for now, it will be managed through code, so just follow the default Oauth client creation steps
- Create OAuth 2.0 credentials (Desktop App)
- Download client secret credentials as json, and place this file in your project root through file explorer or otherwise
- Rename the file client_secret.json in your project root (IMPORTANT)

### 2. Create Telegram Bot

- Message [@BotFather](https://t.me/BotFather)
- Use `/newbot` and follow the prompts
- Save the Bot Token
- Open a chat with your bot and send any message, this is to get the chat id by monitoring updates in the next step
- Get your `chat_id` by visiting:
  ```
  https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates
  ```
- Replace <YOUR_BOT_TOKEN> with your actual token. Look for "chat":{"id":123456789,...} in the JSON response. This number is your chat ID.
- Save the bot token and chat_id in a .env file in your project root, they MUST be named TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID

### 3. Install Dependencies

```bash
pip install google-api-python-client google-auth google-auth-oauthlib requests
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

## ✍️ Filter Customization

Edit the `KEYWORDS` list in `main.py`:

```python
KEYWORDS = ['payment', 'urgent', '2fa']
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

Feel free to fork and extend it!
