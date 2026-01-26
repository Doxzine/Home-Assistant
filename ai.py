from dotenv import load_dotenv
from openai import OpenAI
text = 0
load_dotenv()

client = OpenAI()

resp = client.responses.create(
    model="gpt-5-nano",
    input=text
)
##Prints the response!!!
print(resp.output_text)


