from stt import listen
from tts import speak

speak("ok")


text = listen()



if text:
    print("Heard:", text)
    speak(text)


elif not text:
    print("Didn't catch that")
    speak("I didn't catch that")


#raise systemexit