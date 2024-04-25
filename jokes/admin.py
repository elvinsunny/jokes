from django.contrib import admin

# Register your models here.


# myapp/admin.py
from django.contrib import admin
from .models import Joke

# Register the Joke model
admin.site.register(Joke)
