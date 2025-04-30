from django.db import models
import random

def generate_chat_bot_name():
    return "ChatBot " + random.choice(["Tom", "Jerry", "John", "Jane", "Jim", "Jill"])

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    level = models.IntegerField()
    chat_bot_name = models.CharField(max_length=255)
    

