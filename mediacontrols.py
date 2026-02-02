import logging

from rapidfuzz import fuzz

logger = logging.getLogger(__name__)

COMMAND_PHRASES: dict[str, list[str]] = {
    "pause": ["pause music", "pause", "stop music", "stop song", "pause song"],
    "play": ["play music", "play song", "resume music", "start music"],
    "next": ["next track", "skip", "next song", "skip track", "skip song"],
    "previous": ["previous track", "back song", "go back", "previous song", "last song"],
    "mute": ["mute volume", "unmute volume", "mute", "unmute"],
}

THRESHOLD = 60


def match_command(text: str) -> str | None:
    """Match user text against known media commands using fuzzy matching.

    Returns the command name if the best match exceeds THRESHOLD, else None.
    """
    text = text.lower()

    best_match: str | None = None
    best_score = 0

    for command, phrases in COMMAND_PHRASES.items():
        for phrase in phrases:
            score = fuzz.partial_ratio(text, phrase)
            if score > best_score:
                best_score = score
                best_match = command

    if best_score >= THRESHOLD:
        logger.info("Matched command '%s' (score: %d)", best_match, best_score)
        return best_match

    logger.debug("No command matched (best score: %d)", best_score)
    return None
