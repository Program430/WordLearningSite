from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse
from main.forms import CustomUserCreationForm
from main.models import Word
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib import auth
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
import math

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
    return render(request, login_page)


@login_required(login_url='login')
def word_list(request): 
    return render(request, 'main/word_list/main_word_list.html')

@csrf_exempt
def get_word_list_page_count(request):
    count = { 'count': math.ceil(Word.objects.count() / words_per_page) }
    return JsonResponse(count)

class WordListGetData(View):
    words = Word.objects.all()
    paginator = Paginator(words, words_per_page)
    def get(self, request, page = 1):
        print(self.paginator.page(page))
        return JsonResponse(self.paginator.page(page).object_list)



@login_required(login_url='login')
def word_card(request):
    return render(request, 'main/card/word_card.html')

@login_required(login_url='login')
def user_word_list(request):
    return render(request, 'main/user_word_list/user_word_list.html')
