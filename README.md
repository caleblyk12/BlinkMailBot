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
- Filters emails based on keywords in the sender, subject, or snippet
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

### 1. Enable Gmail API

- Visit: https://console.cloud.google.com/
- Create a project
- Enable Gmail API
- Configure OAuth consent screen (internal for personal use)
- Create OAuth 2.0 credentials (Desktop App)
- Download the `client_secret.json` file and place it in your project root

### 2. Create Telegram Bot

- Message [@BotFather](https://t.me/BotFather)
- Use `/newbot` and follow the prompts
- Save the Bot Token
- Open a chat with your bot and send a message
- Get your `chat_id` by visiting:
  ```
  https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates
  ```

### 3. Install Dependencies

```bash
pip install google-api-python-client google-auth google-auth-oauthlib requests
```

### 4. Run the Bot

```bash
python main.py
```

You'll be asked to log in to your Gmail account and allow read access. After that, the bot starts checking for new emails every 30 seconds and sends matches to Telegram.

## ✍️ Customization

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

---

Feel free to fork and extend it!
