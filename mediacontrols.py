from rapidfuzz import fuzz, process


COMMAND_PHRASES = {
    "pause": ["pause music", "pause", "stop music", "stop song", "pause song"],
    "play": ["play music", "play song", "resume music", "start music"],
    "next": ["next track", "skip", "next song", "skip track", "skip song"],
    "previous": ["previous track", "back song", "go back", "previous song", "last song"],
    "mute": ["mute volume", "unmute volume", "mute", "unmute"],
}

#Tinker with
THRESHOLD = 60  

def match_command(text: str):
    text = text.lower()

    best_match = None
    best_score = 0

    for command, phrases in COMMAND_PHRASES.items():
        for phrase in phrases:
            score = fuzz.partial_ratio(text, phrase)
            if score > best_score:
                best_score = score
                best_match = command

    if best_score >= THRESHOLD:
        return best_match
    return None
