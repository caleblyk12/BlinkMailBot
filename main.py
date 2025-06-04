import time
from google_apis import create_service
from telegram_bot import send_telegram_message

# --- Setup Gmail API ---
CLIENT_SECRET_FILE = 'client_secret.json'
API_NAME = 'gmail'
API_VERSION = 'v1'
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

service = create_service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

# --- Filters ---
KEYWORDS = ['strava', ]  # customize this
PROCESSED_EMAILS = set()  # remember which ones you've already forwarded

def check_emails():
    results = service.users().messages().list(userId='me', labelIds=['INBOX'], maxResults=10).execute()
    messages = results.get('messages', [])

    for msg in messages:
        msg_id = msg['id']
        if msg_id in PROCESSED_EMAILS:
            continue

        full_msg = service.users().messages().get(userId='me', id=msg_id, format='metadata').execute()
        headers = full_msg['payload']['headers']
        subject = next((h['value'] for h in headers if h['name'] == 'Subject'), '(No Subject)')
        sender = next((h['value'] for h in headers if h['name'] == 'From'), '')
        snippet = full_msg.get('snippet', '')
        #debug


        body = f"📨 From: {sender}\nSubject: {subject}\nSnippet: {snippet}"


        if any(k.lower() in body.lower() for k in KEYWORDS):
            send_telegram_message(body)
            PROCESSED_EMAILS.add(msg_id)

# --- Loop forever ---
while True:
    try:
        check_emails()
        #debug
        print('emails checked')
        time.sleep(30)  # check every 30 seconds
    except KeyboardInterrupt:
        print("Stopped.")
        break
    except Exception as e:
        print("Error:", e)
        time.sleep(10)