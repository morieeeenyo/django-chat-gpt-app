from openai import OpenAI
import os
from django.conf import settings


def chat_gpt(prompt):
    client = OpenAI(api_key=settings.OPENAI_API_KEY)
    client.models.list()  # OpenAIのインスタンスを生成

    # APIを使ってリクエストを投げる
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=0,
        max_tokens=300,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        messages=[
            {"role": "user", "content": prompt},
        ],
    )
    response = response.choices[0].message.content
    return response


def create_prompt(input_text, file_name):
    prompt_file = os.path.join(
        settings.BASE_DIR, "utils", "openai", "templates", file_name
    )
    with open(prompt_file, encoding="utf-8") as f:
        file_read = f.read()
    # Chat-GTPへ投げるフォーマットに入力文をセットする。
    prompt = file_read.replace("[input]", input_text)
    return prompt
