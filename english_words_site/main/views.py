from django.http import HttpResponse
from django.shortcuts import render

def login(request):
    return render(request, 'main/login_register/login_register.html')





def word_list(request):
    return render(request, 'main/word_list/main_word_list.html')

def word_card(request):
    return render(request, 'main/card/word_card.html')

def user_word_list(request):
    return render(request, 'main/user_word_list/user_word_list.html')
