from django.contrib import admin
from .models import Game, Score, JavaScriptFile

# Register your models here.
class GameAdmin(admin.ModelAdmin):

    list_display = ('id', 'title', 'sequence')

class ScoreAdmin(admin.ModelAdmin):

    list_display = ('id', 'user', 'time', 'score')


class JavaScriptFileAdmin(admin.ModelAdmin):

    list_display = ('id', 'path', 'game', 'sequence')

admin.site.register(JavaScriptFile, JavaScriptFileAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Score, ScoreAdmin)
