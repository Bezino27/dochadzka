from django.contrib import admin
from .models import Player

class PlayerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Player,PlayerAdmin)
from django.contrib import admin

# Register your models here.
