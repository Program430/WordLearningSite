from django.contrib import admin

from main.models import UserWordsList, Word

admin.site.register(Word)
admin.site.register(UserWordsList)
