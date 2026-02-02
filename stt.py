import logging

import sounddevice as sd
import speech_recognition as sr

logger = logging.getLogger(__name__)

SAMPLE_RATE = 16000
LISTEN_DURATION = 4
CHANNELS = 1
SAMPLE_WIDTH = 2  # bytes per sample (16-bit = 2 bytes)


def listen(duration: int = LISTEN_DURATION) -> str | None:
    """Record audio from the microphone and return recognized text."""
    recognizer = sr.Recognizer()

    logger.info("Listening for %d seconds...", duration)
    audio = sd.rec(
        SAMPLE_RATE * duration,
        samplerate=SAMPLE_RATE,
        channels=CHANNELS,
        dtype="int16",
    )
    sd.wait()

    audio_data = sr.AudioData(audio.tobytes(), SAMPLE_RATE, SAMPLE_WIDTH)

    try:
        text = recognizer.recognize_google(audio_data)
        logger.info("Recognized: %s", text)
        return text
    except sr.UnknownValueError:
        logger.warning("Could not understand audio")
        return None
    except sr.RequestError as e:
        logger.error("Speech recognition API error: %s", e)
        return None
