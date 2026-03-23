# Improved Context-Aware Chatbot

name = None
interest = None
chat_history = []

print("Chatbot: Hello! Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()
    chat_history.append(user_input)

    if user_input == "bye":
        print("Chatbot: Goodbye! 👋")
        break

    elif "hi" in user_input or "hello" in user_input:
        print("Chatbot: Hello! 😊 What's your name?")

    elif "my name is" in user_input:
        name = user_input.split("my name is")[-1].strip()
        print(f"Chatbot: Nice to meet you {name}! What are you interested in?")

    elif "i like" in user_input:
        interest = user_input.split("i like")[-1].strip()
        print(f"Chatbot: Wow! I like {interest} too 😄")

    elif "what is my name" in user_input:
        if name:
            print(f"Chatbot: Your name is {name}")
        else:
            print("Chatbot: I don't know your name yet.")

    elif "what do i like" in user_input:
        if interest:
            print(f"Chatbot: You like {interest}")
        else:
            print("Chatbot: I don't know your interest yet.")

    else:
        print("Chatbot: Sorry, I didn't understand that.")