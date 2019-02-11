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
    my_dict = {
        'dinner': dinner,
        'box' : box,
    }
    return render(request, 'dinner.html', my_dict)
    # template은 기본적으로 문밥이 jinja2랑 같지만, 장고에서는 DTL을 쓴다.
def you(request, name):
    return render(request, 'you.html', {'name': name})
    
def cube(request, num):
    return render(request, 'cube.html', {'num': num**3 })