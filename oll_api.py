import requests

url = "http://localhost:11434/api/chat"

response = requests.post(
    url,
    json={
        "model": "llama3.2",
        "messages": [
            {
                "role": "user",
                "content": input("Enter your prompt: ")
            }
        ]
    }
)
print(type(response))
print(response.status_code)