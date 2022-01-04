from django.shortcuts import render
from django.http import HttpResponseRedirect
#from tempapps.forms import QuestionForm

#tempapps의 바로가기 화면: 바로가기 링크만 있음 
def index(request):
    return render(request, 'index.html')

# Template Filter를 사용하기 위한 여러종류의 변수 선언 및 Template 호출
def templateFilter(request):
    #정수형 변수
    num1 = 1
    num2 = 10
    
    #문자형 변수
    engStr = "nakja's MustHave\r\n java <b>web</b> programming"
    hanStr = "낙자쌤의 자바 웹 프로그래밍"
    #컬렉션형 변수
    dictVar = {'a':'유비', 'b':'관우', 'c':'장비'} #딕셔너리
    listVar =['손오공', '저팔계', '사오정']# 리스트
    
    context = {'num1' : num1, 'num2': num2, 'engStr': engStr, 'hanStr' : hanStr,
               'dictVar ': dictVar , 'listVar': listVar}
    #템플릿 호출 및 값 전달
    return render(request, 'template_filter.html', context) 
# Create your views here.
