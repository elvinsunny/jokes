from django.db import models

# Create your models here.


# models.py
from django.db import models

class Joke(models.Model):
    text = models.TextField()
    language = models.CharField(max_length=100)
