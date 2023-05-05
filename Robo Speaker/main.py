import pyttsx3

engine = pyttsx3.init()

if __name__ == "__main__":
    while True:
        command = input('Enter the command you want me to say : ')
        if command == "q":
            break
        engine.say(command) 
        engine.runAndWait()