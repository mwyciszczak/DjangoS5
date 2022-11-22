from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Film)
admin.site.register(User)
admin.site.register(Entry)