from django.shortcuts import render, HttpResponse
import random

# Create your views here.
def index(request):
    return render(request, 'index.html')
    
def dinner(request):
    box = ['치킨', '치킨', '치킨', '와퍼']
    dinner = random.choice(box)
    
    # render 필수인자
    # 1) request, 2) template 파일(html)
    # render 선택인자
    # 3) dictionary : 템플릿에서 쓸 변수 값을 정의
    return render(request, 'dinner.html', {'dinner': dinner})