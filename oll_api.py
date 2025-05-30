import requests

url = "http://localhost:11434/api/chat"

response = requests.post(
    url,
    json={
        "model": "mistral",
        "messages": [
            {
                "role": "user",
                "content": input("Enter your prompt: ")
            }
        ]
    },
    stream=True
)

for line in response.iter_lines():
    
        print(line.decode('utf-8'))