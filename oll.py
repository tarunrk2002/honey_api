import ollama

client = ollama.Client()

response = client.generate(
    model="llama3.2",
    prompt= input("Enter your prompt: "))

print(response.response)
