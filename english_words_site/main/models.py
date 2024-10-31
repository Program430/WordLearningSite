from django.db import models
from django.contrib.auth.models import User


class Word(models.Model):
    english = models.CharField(max_length=15, unique=True, db_index=True)
    russian = models.CharField(max_length=15)


class UserWordsList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
