from django.contrib import admin

from .models import Greeting, Url


admin.site.register(Greeting)
admin.site.register(Url)

