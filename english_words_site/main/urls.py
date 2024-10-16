
from django.urls import path
from main.views import login, word_list, word_card, user_word_list

urlpatterns = [
    path('login/', login, name= 'login'),
    path('word_list/', word_list, name= 'word_list'),
    path('word_card/', word_card, name= 'word_card'),
    path('user_word_list/', user_word_list, name= 'user_word_list'),
]