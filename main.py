import logging

import pyautogui

from stt import listen
from tts import speak
from ai import ai
from mediacontrols import match_command

logger = logging.getLogger(__name__)

# Map command names to (keyboard_key, spoken_confirmation)
MEDIA_ACTIONS: dict[str, tuple[str, str]] = {
    "pause": ("playpause", "Paused"),
    "play": ("playpause", "Resumed"),
    "next": ("nexttrack", "Next track"),
    "previous": ("prevtrack", "Going back"),
    "mute": ("volumemute", "Toggled mute"),
}


def handle_media_command(command: str) -> bool:
    """Execute a media command if recognized. Returns True if handled."""
    if command not in MEDIA_ACTIONS:
        return False

    key, confirmation = MEDIA_ACTIONS[command]
    pyautogui.press(key)
    speak(confirmation)
    return True


def main() -> None:
    """Run one cycle of the voice assistant: listen, match, respond."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(name)s] %(levelname)s: %(message)s",
    )

    speak("ok")

    text = listen()
    if not text:
        logger.warning("No speech detected")
        speak("I didn't catch that")
        return

    logger.info("You said: %s", text)

    # Try media commands first
    command = match_command(text)
    if command and handle_media_command(command):
        return

    # Fall back to AI response
    response = ai(text)
    logger.info("AI response: %s", response)
    speak(response)


if __name__ == "__main__":
    main()
