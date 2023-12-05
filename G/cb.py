import random

def get_response(user_input):
    responses = {
        "hello": "Hi there! How can I help you?",
        "how are you": "I'm just a computer program, but thanks for asking!",
        "bye": "Goodbye! Have a great day.",
        "default": "I'm not sure how to respond to that. Can you ask me something else?"
    }

    return responses.get(user_input.lower(), responses["default"])

def main():
    print("Simple Python Chatbot")
    print("Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye!")
            break

        response = get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
