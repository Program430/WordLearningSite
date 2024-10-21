
from django.urls import path
from main.views import WordListGetData, login, word_list, word_card, user_word_list, register, logout, get_word_list_page_count

urlpatterns = [
    path('login/', login, name = 'login'),
    path('register/', register, name = 'register'),
    path('logout/', logout, name = 'logout'),

    path('word_list/', word_list, name = 'word_list'),
    path('word_list/count/', get_word_list_page_count, name = 'get_word_list_page_count'),
    path('word_list/<int:page>/', WordListGetData.as_view(), name = 'word_list_get_data'),

    path('word_card/', word_card, name = 'word_card'),
    path('user_word_list/', user_word_list, name = 'user_word_list'),
]