import os
from dotenv import load_dotenv
from src.google_sheets import get_form_responses
from src.whatsapp_sender import send_whatsapp_message
from src.utils import format_response

load_dotenv()

def main():
    responses = get_form_responses()
    phone_number = os.getenv("DEST_PHONE_NUMBER")
    for response in responses:
        message = format_response(response)
        send_whatsapp_message(phone_number, message)

if __name__ == "__main__":
    main()