import datetime

def chatbot():
    print("🤖 Chatbot: Hello! I am your basic chatbot.")
    print("Type 'bye' to exit.\n")

    name = ""

    while True:
        user_input = input("You: ").lower()

        # Greetings
        if user_input in ["hello", "hi", "hey"]:
            print("🤖 Chatbot: Hello there!")

        # Asking chatbot status
        elif user_input in ["how are you", "how are you?"]:
            print("🤖 Chatbot: I'm fine, thanks! How can I help you?")

        # Asking name
        elif "my name is" in user_input:
            name = user_input.replace("my name is", "").strip()
            print(f"🤖 Chatbot: Nice to meet you, {name.capitalize()}!")

        elif user_input == "what is my name":
            if name:
                print(f"🤖 Chatbot: Your name is {name.capitalize()}.")
            else:
                print("🤖 Chatbot: I don't know your name yet.")

        # Time
        elif user_input == "time":
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"🤖 Chatbot: Current time is {current_time}")

        # Help
        elif user_input == "help":
            print("🤖 Chatbot: You can say hello, ask time, tell me your name, or say bye.")

        # Thank you
        elif user_input in ["thanks", "thank you"]:
            print("🤖 Chatbot: You're welcome!")

        # Joke
        elif user_input == "tell me a joke":
            print("🤖 Chatbot: Why do programmers prefer dark mode? Because light attracts bugs! 😄")

        # Exit
        elif user_input == "bye":
            print("🤖 Chatbot: Goodbye! Have a great day 😊")
            break

        else:
            print("🤖 Chatbot: Sorry, I don't understand that.")

# Run chatbot
chatbot()
