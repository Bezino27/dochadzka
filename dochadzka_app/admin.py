from django.contrib import admin
from .models import Player, Training, Category

class PlayerAdmin(admin.ModelAdmin):
    pass

class TrainingAdmin(admin.ModelAdmin):
    list_display = ('day', 'date', 'time', 'category')
    filter_horizontal = ('player',)  # Umožní výber viacerých hráčov v admin paneli

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'year')
    filter_horizontal = ('player', 'training')

admin.site.register(Player,PlayerAdmin)
admin.site.register(Training, TrainingAdmin)
admin.site.register(Category, CategoryAdmin)
from django.contrib import admin

# Register your models here.

