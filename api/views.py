from django.shortcuts import render
from rest_framework import viewsets, views
from .models import Threads
from django.http import HttpResponse
from .serializers import ThreadSerializer
import sys
import json

sys.path.append("../")
from utils.openai.create_message import chat_gpt, create_prompt

# Create your views here.


class ThreadViewSet(viewsets.ModelViewSet):
    queryset = Threads.objects.all()
    serializer_class = ThreadSerializer


class MessageView(views.APIView):
    def post(self, request):
        # 画面に入力した文章を取得
        input_text = request.POST["input_text"]
        # Chat-GPTに投げる命令文を生成
        prompt = create_prompt(input_text, "GrammarCorrection.txt")
        # Chat-GPTへリクエストを投げる
        response = chat_gpt(prompt)
        # 辞書型データを作成する
        response_obj = {"data": response}
        json_str = json.dumps(response_obj, ensure_ascii=False, indent=2)
        return HttpResponse(json_str)
