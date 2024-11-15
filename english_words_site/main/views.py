import json
import time
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse
from main.forms import CustomUserCreationForm
from main.models import Word, UserWordsList
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib import auth
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
import math, threading, queue
from googletrans import Translator
from mytools.get_ai_answer import get_data_about_word_through_proxy

login_page = 'main/login_register/login_register.html'
words_per_page = 10

def register(request):
    if request.method == 'POST':
        request_data = {
            'username': request.POST.get('rname'),
            'password': request.POST.get('rpassword'),
            'email': request.POST.get('remail'),
        }

        form = CustomUserCreationForm(data = request_data)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return redirect(reverse('word_list'))
    
    return render(request, login_page)


def login(request):
    if request.method == 'POST':
        request_data = {
            'username': request.POST.get('lname'),
            'password': request.POST.get('lpassword'),
        }

        form = AuthenticationForm(data = request_data)
        user = auth.authenticate(username = request_data['username'],
                             password = request_data['password'])
        if user:
            auth.login(request,user)
            return redirect(reverse('word_list'))

    return render(request, login_page)

def logout(request):
    auth.logout(request) 
    return redirect(reverse('login'))


@login_required(login_url='login')
def word_list(request): 
    return render(request, 'main/word_list/main_word_list.html')


@login_required(login_url='login')
def get_word_list_page_count(request):
    count = { 'count': math.ceil(Word.objects.count() / words_per_page) }
    return JsonResponse(count)

class WordListGetData(LoginRequiredMixin, View):
    words = Word.objects.all()
    paginator = Paginator(words, words_per_page)
    def get(self, request, page = 1):
        try:
            page_object = self.paginator.page(page)
        except:
            page_object = self.paginator.page(self.paginator.num_pages)
        word_list = [word.english for word in page_object.object_list]
        return JsonResponse({'word_list': word_list})

@login_required(login_url='login')
def word_card(request, word, list):
    word = get_object_or_404(Word, english=word)

    ai_request = f'''Что занчит {word.english}?3-5 предложения. Ответ только на русском'''

    description = get_data_about_word_through_proxy(ai_request)

    print(description)

    return render(request, 'main/card/word_card.html', context = {'en': word.english, 'ru':word.russian,
                                                                   'description':description, 'user_list': list})


class UserWords:
    @login_required(login_url='login')
    def user_word_list(request):
        context = [word.word.english for word in UserWordsList.objects.filter(user = request.user).select_related('word')]
        return render(request, 'main/user_word_list/user_word_list.html', context={'context':context})

    class WordListAddWord(LoginRequiredMixin, View):
        def post(self, request):
            try:
                body_unicode = request.body.decode('utf-8')
                body_data = json.loads(body_unicode)  
                word = body_data.get('english')
                word = Word.objects.get(english = word)
                UserWordsList.objects.get_or_create(word = word, user = request.user)
            except:
                return JsonResponse({'status':'Error'}, status=400)
            return JsonResponse({'status':'Success'}, status=200)

    class WordListDeleteWord(LoginRequiredMixin, View):
        def post(self, request): 
            body_unicode = request.body.decode('utf-8')
            body_data = json.loads(body_unicode)  
            word = body_data.get('english')
            word = Word.objects.get(english = word)
            UserWordsList.objects.filter(word = word, user = request.user).delete()
            
            return JsonResponse({'status':'Success'}, status=200)

    class WordListCheckWord(LoginRequiredMixin, View):
        def post(self, request):
            body_unicode = request.body.decode('utf-8')
            body_data = json.loads(body_unicode)  
            word = body_data.get('english')
            word = Word.objects.get(english = word)
            exists = UserWordsList.objects.filter(word = word, user = request.user).exists()
            if exists:
                return JsonResponse({'statusB':'Yes'}, status=200)
            return JsonResponse({'statusB':'No'}, status=400)


@login_required(login_url='login')
def get_train_page(request):
    return render(request, 'main/train/train.html')


@login_required(login_url='login')
def get_train_data_user(request):
    user_word_list = [{'en':word.word.english, 'ru':word.word.russian} 
                      for word in UserWordsList.objects.filter(user = request.user).select_related('word')]
    return JsonResponse({'data': user_word_list}, status=200)

@login_required(login_url='login')
def get_train_data_full_list(request):
    word_list = [{'en':word.english, 'ru':word.russian} for word in Word.objects.order_by('?')[:10]]
    return JsonResponse({'data': word_list}, status=200)

    

