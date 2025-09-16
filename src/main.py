import os
import time
from dotenv import load_dotenv
from src.google_sheets import get_form_responses
from src.whatsapp_sender import send_whatsapp_message
from src.utils import format_response

load_dotenv()

def main():
    last_count = 0
    while True:
        responses = get_form_responses()
        if len(responses) > last_count:
            new_responses = responses[last_count:]
            phone_number = os.getenv("DEST_PHONE_NUMBER")
            for response in new_responses:
                message = format_response(response)
                send_whatsapp_message(phone_number, message)
            last_count = len(responses)
        time.sleep(60) 

if __name__ == "__main__":
    main()