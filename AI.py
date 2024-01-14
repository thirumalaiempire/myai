import requests

url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=AIzaSyDzlUyv9sIbNu3zeQ-n495Stbg0l2rKmHg'

def bard(inp):
    
    payload = {
        "contents": [{"parts": [{"text": f"{inp}"}]}]
    }

    headers = {
        'Content-Type': 'application/json'
    }
    res = requests.post(url, json=payload, headers=headers)

    result = res.json()['candidates'][0]['content']['parts'][0]['text']
    
    return result

# if __name__ == "__main__":
#     print(bard())