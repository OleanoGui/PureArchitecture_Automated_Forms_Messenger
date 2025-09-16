import json

def format_response(response):
    return json.dumps(response, ensure_ascii=False, indent=2)