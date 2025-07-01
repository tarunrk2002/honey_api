import requests
import tensorflow as tf

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
       
    if line:
       print(line.decode('utf-8'))

# gpus = tf.config.list_physical_devices('GPU')
# if gpus:
#       print(f"GPU detected: {gpus}")
# else:
#       print("No GPU found.") 