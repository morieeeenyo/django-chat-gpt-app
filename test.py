
from openai import OpenAI

APK_KEY = ""

client = OpenAI(api_key=APK_KEY)

def chat_gpt(prompt):
     #API KEYをセット
    client.models.list() #OpenAIのインスタンスを生成
  
    #APIを使ってリクエストを投げる
    response = client.completions.create(model = "text-davinci-003",
    prompt= prompt,
    temperature=0,
    max_tokens=300,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0)
    return response 