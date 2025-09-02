import os
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()

ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
FROM_WHATSAPP_NUMBER = os.getenv('TWILIO_FROM_WHATSAPP_NUMBER')

def send_whatsapp_message(phone_number: str, message: str):
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    try:
        message = client.messages.create(
            body=message,
            from_=FROM_WHATSAPP_NUMBER,
            to=f'whatsapp:{phone_number}'
        )
        print(f"Message sent to {phone_number}. SID: {message.sid}")
    except Exception as e:
        print(f"Failed to send message to {phone_number}: {e}")