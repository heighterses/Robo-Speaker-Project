import os
import pyttsx3

engine = pyttsx3.init()
print("Welcome to Robo Speaker")
print()
while True:
    text = input("Enter here To Speak: ").lower()
    if text == "End":
        print("You have pressed 'End' for Exit")
        break
    engine.say(text)
    engine.runAndWait()

'''if __name__ == '__main__':
    print("Welcome to Robo Speaker 1.1- ")
    x = input("What do you want me to speak: ")
    command = f" say {x}"
    os.system(command)'''
