from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import NewDog

admin.site.register(NewDog)

from .models import Account

admin.site.register(Account)