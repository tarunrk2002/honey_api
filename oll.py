import ollama

client = ollama.Client()

response = client.generate(
    model="mistral",
    prompt= input("Enter your prompt: "))

print(response.response)
