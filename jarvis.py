
import pyttsx3
import speech_recognition as sr
import wolframalpha
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
from commands import getCommand
from modules import goodbye , speak, takeCommand

# Initialize the ChatBot
def initialize_chatbot():
    bot = ChatBot('Jarvis')
    # trainer = ListTrainer(bot)
    # corpus_trainer = ChatterBotCorpusTrainer(bot)
    # corpus_trainer.train('chatterbot.corpus.english')

    with open('Data/chats.txt', 'r') as file:
        data = file.readlines()
        # trainer.train(data)

    print("[Training Process complete]")

    try:
        app = wolframalpha.Client("YOUR_OPENAI_API_KEY")
    except Exception:
        print("not working")

    return bot, app

bot, app = initialize_chatbot()

commands = getCommand()

def process_command(command):
    # Check if the command matches any of the recognized command phrases
    for cmd_phrase, cmd_info in commands.items():
        if any(phrase.lower() in command.lower() for phrase in cmd_info["phrases"]):
            # Execute the command immediately if it doesn't require a query
            if not cmd_info["requires_query"]:
                try:
                    cmd_info["function"]()
                    return  # Exit the function after executing the command
                except Exception as e:
                    print(f"An error occurred: {e}")

            # If the command requires a query, try to extract it
            query = extract_query(command, cmd_info["phrases"])
            if query:
                try:
                    cmd_info["function"](query)
                except Exception as e:
                    print(f"An error occurred: {e}")
            else:
                speak("Please specify a query for this command.")
            return  # Exit the function after processing the recognized command

    # If the command doesn't match any recognized phrases, try other processing methods
    try:
        res = app.query(command)
        speak(next(res.results).text)
    except Exception as e:
        print(f"An error occurred: {e}")
        speak("Sorry, I am unable to process your request.")


def extract_query(command, phrases):
    for phrase in phrases:
        command = command.replace(phrase, "").strip()

    return command

def handle_user_commands():
    while True:
        query = takeCommand().lower()
        if query == 'none':
            continue

        if query:
            process_command(query)

if __name__ == "__main__":
    while True:
        permission = takeCommand().lower()
        if "wake up jarvis" in permission or "activate jarvis" in permission:
            speak("hello at your services")
            handle_user_commands()
        elif 'goodbye' in permission:
            goodbye()
