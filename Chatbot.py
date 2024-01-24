def get_response(user_input):
    #convert user input to lower case to make it case insensitive
    user_input = user_input.lower()

    #define rule and responses
    if "hello" in user_input:
        return "Hi there! How can i help you?"
    
    elif "how are you" in user_input:
        return "I am doing well. What about you?"
    
    elif "goodbye" in user_input:
        return "Goodbye! Have a nice day"
    
    else:
        return "I'm not sure how to respond. Sorry"
    
def main():
    print("Rule-Based Chatbot: Type 'bye' to exit.")

    while True:
        user_input = input('You: ')
        if user_input.lower() == 'bye':
            print("ChatBot: GoodBye!")
            break

        response = get_response(user_input)
        print("ChatBot: ", response)

if __name__=="__main__":
    main()