from django.contrib import admin
from .models import Novel

@admin.register(Novel)
class NovelAdmin(admin.ModelAdmin):
    list_display       = ['title', 'type', 'structure', 'last_update', 'n_likes', 'n_dislikes', 'n_views']
    ordering           = ['title']
    readonly_fields    = ('creation_date', 'last_update', 'n_likes', 'n_dislikes', 'n_views')
    list_display_links = ['title']
    list_filter        = ('type', 'structure', 'creation_date')
    ordering           = ['title']
    search_fields      = ['title']
    
    show_full_result_count = True
