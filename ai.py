from dotenv import load_dotenv
from openai import OpenAI
text = 0
load_dotenv()

client = OpenAI()

def ai(text: str) -> str:
    response = client.responses.create(
        model="gpt-5-nano",
        instructions="""
        You are a home assistant.
        Respond in briefly
        Do not ask questions.
        Be direct.

        """,
        input = text,
        
    )
    return response.output_text



