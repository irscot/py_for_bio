import pyttsx3
import cowsay

# initializing the pyttsx3 with a variable engine
engine = pyttsx3.init()

text = "Eat Mor Chikin!"

engine.say(text)
cowsay.cow(text)

# play the speech
engine.runAndWait()