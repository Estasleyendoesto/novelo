from django.contrib import admin
from .models import Novel

@admin.register(Novel)
class NovelAdmin(admin.ModelAdmin):
    list_display    = ['pk', 'title', 'type', 'structure', 'date_updated', 'n_likes', 'n_dislikes', 'n_views']
    ordering        = ['pk', 'title']
    readonly_fields = ('date_created', 'date_updated', 'n_likes', 'n_dislikes', 'n_views')
