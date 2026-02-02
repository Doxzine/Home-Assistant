import logging

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

logger = logging.getLogger(__name__)
client = OpenAI()

SYSTEM_PROMPT = (
    "You are a home assistant. "
    "Respond briefly. "
    "Do not ask questions. "
    "Be direct."
)


def ai(text: str) -> str:
    """Send user text to the AI model and return the response."""
    logger.info("Sending query to AI: %s", text)
    response = client.responses.create(
        model="gpt-5-nano",
        instructions=SYSTEM_PROMPT,
        input=text,
    )
    return response.output_text

