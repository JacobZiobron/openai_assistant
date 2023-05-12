import openai
import os
from dotenv import load_dotenv
import pyperclip as clip
import time

load_dotenv()

def write_query(base_prompt):
    # get environment variables
    Api_Key = os.getenv('OPENAI_API_KEY')
    Model_Engine = os.getenv('MODEL_ENGINE')
    Temperature = float(os.getenv("TEMPERATURE"))
    Max_Tokens = int(os.getenv("MAX_TOKENS"))

    # set API key
    openai.api_key = Api_Key

    # generate text from prompt
    complete_prompt = str(base_prompt) + str(clip.paste()) + '"'
    completion = openai.Completion.create(engine=Model_Engine, prompt=complete_prompt, max_tokens=Max_Tokens, n=1,stop=None,temperature=Temperature)

    # Need to wait for the API request to complete
    time.sleep(5)
    message = completion.choices[0].text

    clip.copy(message)
    print("Message copied to clipboard.")