import pyttsx3

def speak(text: str):
    engine = pyttsx3.init()
    engine.setProperty("rate", 180)
    engine.setProperty("volume", 1.0)
    engine.say(str(text))
    engine.runAndWait()
    engine.stop()
