from stt import listen
from tts import speak
from ai import ai
from mediacontrols import match_command
import pyautogui


##Listening start
speak("ok")


text = listen()

if not text:
    print("Didn't catch that")
    speak("I didn't catch that")
    exit()

command = match_command(text)

if command == "pause":
    pyautogui.press("playpause")
    speak("Paused")
    exit()

elif command == "play":
    pyautogui.press("playpause")
    speak("Resumed")
    exit()

elif command == "next":
    pyautogui.press("nexttrack")
    speak("Next track")
    exit()

elif command == "previous":
    pyautogui.press("prevtrack")
    speak("Going back")
    exit()
    
elif command == "mute":
    pyautogui.press("volumemute")
    print("Toggled mute")
    exit()


print(text)
print(f"You: {text}")
airesponse = ai(text)
print(f"AI Response: {airesponse}")
speak(airesponse)
    
#raise systemexit