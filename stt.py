import sounddevice as sd
import speech_recognition as sr

SAMPLE_RATE = 16000

def listen(duration=4) -> str | None:
    r = sr.Recognizer()

    print("Listening...")
    audio = sd.rec(
        SAMPLE_RATE * duration,
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype='int16'
    )
    sd.wait()

    audio_data = sr.AudioData(
        audio.tobytes(),
        SAMPLE_RATE,
        2
    )

    try:
        return r.recognize_google(audio_data)
    except sr.UnknownValueError:
        return None
    except sr.RequestError as e:
        print("STT error:", e)
        return None
