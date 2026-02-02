import logging

import pyttsx3

logger = logging.getLogger(__name__)

SPEECH_RATE = 180
SPEECH_VOLUME = 1.0


def speak(text: str) -> None:
    """Convert text to speech and play it through the default audio output."""
    logger.info("Speaking: %s", text)
    engine = pyttsx3.init()
    engine.setProperty("rate", SPEECH_RATE)
    engine.setProperty("volume", SPEECH_VOLUME)
    engine.say(text)
    engine.runAndWait()
    engine.stop()
