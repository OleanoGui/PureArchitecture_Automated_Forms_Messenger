from src.google_sheets import get_form_responses

def main():
    responses = get_form_responses()
    for response in responses:
        print(response)

if __name__ == "__main__":
    main()