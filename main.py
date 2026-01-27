from stt import listen
from tts import speak
from ai import ai

speak("ok")


text = listen()



if text:
    print(text)
    print(f"You: {text}")
    airesponse = ai(text)
    print(f"AI Response: {airesponse}")
    speak(airesponse)
    
    


elif not text:
    print("Didn't catch that")
    speak("I didn't catch that")


#raise systemexit