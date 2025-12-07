import os
import os
from dotenv import load_dotenv
from scraper import get_website_content
from openai import OpenAI



load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')

openai = OpenAI()

if not api_key:
    print("No API Key was found")


system_prompt = """
You are a fast website analyzer that reads a webpage and explains in simple words what the business does. Summarize the website clearly, focusing on its industry, services/products, target audience, and how it helps customers. Ask what the user is searching for (e.g., looking for a service provider, product, consultation, membership, etc.). Compare the user’s need with the website’s offer: if it matches, recommend proceeding and provide clear call-to-action details like contact info or buttons; if it does not match, briefly say it’s not a fit and suggest why. Always respond concisely, helpful, and without extra fluff.
"""

user_prompt = """
I am looking for Remote AI engineer. check if this person is right
"""




def summarize(url):
    web_content = get_website_content(url)
    response = openai.chat.completions.create(
        model="gpt-5-nano",
        messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt + web_content }
    ]
    )
    print(response.choices[0].message.content)
   


summarize("https://prabhjotsingh.in/")
