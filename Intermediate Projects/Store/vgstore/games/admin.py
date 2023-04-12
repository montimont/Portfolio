from django.contrib import admin
from .models import Genre, Game
# Register your models here.


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'platform', 'genre', 'number_in_stock')


admin.site.register(Genre, GenreAdmin)
admin.site.register(Game, GameAdmin)
