
from django.urls import path
from main.views import WordListGetData, get_train_data_full_list, get_train_data_user, get_train_page, login, word_list, word_card, register, logout, get_word_list_page_count, UserWords

urlpatterns = [
    path('login/', login, name = 'login'),
    path('register/', register, name = 'register'),
    path('logout/', logout, name = 'logout'),

    path('word_list/', word_list, name = 'word_list'),
    path('word_list/count/', get_word_list_page_count, name = 'get_word_list_page_count'),
    path('word_list/<int:page>/', WordListGetData.as_view(), name = 'word_list_get_data'),

    path('word_card/<str:word>/<str:list>/', word_card, name = 'word_card'),

    path('user_word_list/', UserWords.user_word_list, name = 'user_word_list'),
    path('user_word_list/add/', UserWords.WordListAddWord.as_view(), name = 'user_word_list_add'),
    path('user_word_list/delete/', UserWords.WordListDeleteWord.as_view(), name = 'user_word_list_delete'),
    path('user_word_list/check/', UserWords.WordListCheckWord.as_view(), name = 'user_word_list_check'),

    path('train/', get_train_page, name='train'),
    path('get_train_data_user/', get_train_data_user, name='get_train_data_user'),
    path('get_train_data_full_list/', get_train_data_full_list, name='train_data_full_list'),
]


# delete user word
# add user word
# show user words