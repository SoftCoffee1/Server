from dotenv import load_dotenv
import openai
import os

load_dotenv()
try :
    openai.api_key = os.getenv("OPENAI_API_KEY")
    messages = [
        {"role": "system", "content": "Your role is to summarize the article, extract keywords, and respond appropriately to the format."},
        {"role": "system", "content": "I'm trying to search for articles using the Naver API through the very keywords you extracted. Can you extract keywords by referring to this point?"},
        {"role": "user", "content": "title: "},
        {"role": "user", "content": "scripts:"},
        {"role": "user", "content": "Summarize this article in Korean. Additionally extract up to three keywords from the article in Korean"},
        {"role": "assistant", "content": "Could you give it in JSON format with 'summary' and 'keywords' as key?"}
    ]

    answer = ""
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages,
        temperature = 0,
    )
    answer = response['choices'][0]['message']['content']
    print(answer)
except Exception as e :
    print(e)