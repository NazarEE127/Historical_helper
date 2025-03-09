from django.shortcuts import render
from .models import EventWar, EventCompany, Chat
from django.http import HttpResponse
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone
import requests


# Форма регистрации пользователя
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# Форма авторизации пользователя
class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


# Главная страница
def index(request):
    return render(request, 'index.html')


# Отображение всех событий ВОВ
def events_list_war(request):
    events = []
    if request.method == "POST":
        title = request.POST.get('title')
        eventsw = EventWar.objects.all()
        for el in eventsw:
            if title in el.title:
                events.append(el)
    else:
        events = EventWar.objects.all()
    return render(request, 'event_list_war.html', {'events': events})


# Отображения одного определённого события ВОВ
def event_war(request, id):
    event = get_object_or_404(EventWar, id=id)
    return render(request, 'event_war.html', {'event': event})


# Отображения всех событий ПАО Татнефть
def events_list_company(request):
    events = []
    if request.method == "POST":
        title = request.POST.get('title')
        eventsw = EventCompany.objects.all()
        for el in eventsw:
            if title in el.title:
                events.append(el)
    else:
        events = EventCompany.objects.all()
    return render(request, 'event_list_company.html', {'events': events})


# Отображения одного определённого события ПАО Татнефть
def event_company(request, id):
    event = get_object_or_404(EventCompany, id=id)
    return render(request, 'event_company.html', {'event': event})


# Фунция для запроса ответа у YAGPT
def ask_yagpt(question):
    prompt = {
        "modelUri": "gpt://b1gv60cikrkjbv24gd2e/yandexgpt-lite",
        "completionOptions": {
            "stream": False,
            "temperature": 0.6,
            "maxTokens": "2000"
        },
        "messages": [
            {
                "role": "system",
                "text": "Ты исторический помощник по событиям Великой Отечественной войны и истории ПАО Татнефть, "
                        "помогаешь формировать краткие очерки на заданные темы и помогаешь отвечать на вопросы по ВОВ и"
                        "истории ПАО Татнефть, никогда не даёшь такой ответ "
                        "'В интернете есть много сайтов с информацией на эту тему. "
                        "[Посмотрите, что нашлось в поиске](https://ya.ru)',всегда нормальное отвечаешь, "
                        "для ответов можешь использовать эти базы данных: "
                        f"История ВОВ - https://zabrab75.ru/articles/no-articles_category/1941-1945-klyuchevye-sobytiya-velikoj-otechestvennoj-vojny/, "
                        f"История ПАО Татнефть - https://www.tatneft.ru/o-kompanii/history"
            },
            {
                "role": "user",
                "text": question
            }
        ]
    }

    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Api-Key AQVN2XcYp7xb_DnkSPEp7VG_1vJPYY6Ju5f5IvZh"
    }

    response = requests.post(url, headers=headers, json=prompt)
    result = response.json()["result"]["alternatives"][0]["message"]['text']
    return result


# Страница чата с ИИ
@login_required
def ai_chat(request):
    all_questions = Chat.objects.filter(user_id=request.user.id)
    print(all_questions)
    if request.method == "POST":
        user_input = request.POST.get('message-input')
        ai_response = ask_yagpt(user_input).replace("\n", "\\n")
        chat = Chat.objects.create(user_question=user_input, user_id=request.user.id,
                                   date_time=timezone.now(), ai_answer=ai_response)
        return render(request, 'ai_chat.html',
                      {'all_questions': all_questions})
    return render(request, 'ai_chat.html', {'all_questions': all_questions})


# Очишение чата
def delete_questions(request):
    all_questions = Chat.objects.filter(user_id=request.user.id)
    for ques in all_questions:
        ques.delete()
    return redirect("ai_chat")


# Регистрация пользователя
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Перенаправление на главную страницу после успешной регистрации
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


# Авторизация пользователя
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Перенаправление на главную страницу после успешного входа
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


# Выход из аккаунта пользователя
def logout_view(request):
    logout(request)
    return redirect('home')

