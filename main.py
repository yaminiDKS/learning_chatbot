import random
import pickle
import os

class SimpleChatbot:
    def __init__(self, data_file='chatbot_data.pkl'):
        self.data_file = data_file
        self.responses = self.load_data()

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'rb') as file:
                return pickle.load(file)
        else:
            return {}

    def save_data(self):
        with open(self.data_file, 'wb') as file:
            pickle.dump(self.responses, file)

    def learn(self, user_input, bot_response):
        self.responses[user_input.lower()] = bot_response
        self.save_data()

    def get_response(self, user_input):
        user_input = user_input.lower()
        if user_input in self.responses:
            return self.responses[user_input]
        else:
            return "I don't know how to respond to that. What should I say?"

    def interact(self):
        print("Hello! I am a learning chatbot. (type 'exit' to stop)")
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                print("Goodbye!")
                break
            response = self.get_response(user_input)
            print(f"Bot: {response}")
            if response.startswith("I don't know how to respond"):
                new_response = input("You can teach me! What should I respond? ")
                self.learn(user_input, new_response)
                print("Thank you! I've learned something new.")

if __name__ == "__main__":
    bot = SimpleChatbot()
    bot.interact()
