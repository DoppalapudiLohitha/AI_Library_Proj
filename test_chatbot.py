from chatbot import chat

while True:
    question = input("You: ")

    if question.lower() == "quit":
        break

    print("Bot:", chat(question))