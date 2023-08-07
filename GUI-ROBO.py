import pyttsx3
import tkinter as tk
from PIL import ImageTk, Image

def speak_text():
    text = text_entry.get()
    engine.say(text)
    engine.runAndWait()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Create the main window
window = tk.Tk()
window.title("Text-to-Speech Robot")

# Load the robot image
'''robot_image = Image.open("robot.png")
robot_image = robot_image.resize((200, 200), Image.ANTIALIAS)
robot_photo = ImageTk.PhotoImage(robot_image)'''

# Create a label with the robot image
'''image_label = tk.Label(window, image=robot_photo)
image_label.pack()'''

# Create a label
label = tk.Label(window, text="Enter text:", font=("Arial", 16))
label.pack()

# Create an entry field
text_entry = tk.Entry(window, font=("Arial", 14), width=30)
text_entry.pack()

# Create a button
button = tk.Button(window, text="Speak", font=("Arial", 14), command=speak_text)
button.pack()

# Start the main event loop
window.mainloop()
