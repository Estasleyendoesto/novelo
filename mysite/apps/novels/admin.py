from django.contrib import admin
from .models import Novel, Volume, Chapter, Illustration

@admin.register(Novel)
class NovelAdmin(admin.ModelAdmin):
    list_display       = ['title', 'type', 'structure', 'last_update', 'n_likes', 'n_dislikes', 'n_views']
    ordering           = ['title']
    readonly_fields    = ('creation_date', 'last_update', 'n_likes', 'n_dislikes', 'n_views')
    list_display_links = ['title']
    list_filter        = ('type', 'structure', 'creation_date')
    search_fields      = ['title']
    
    show_full_result_count = True


@admin.register(Volume)
class VolumeAdmin(admin.ModelAdmin):
    list_display       = ['title', 'number', 'novel_id', 'creation_date', 'last_update', 'n_likes', 'n_dislikes', 'n_views']
    ordering           = ['title', 'number']
    readonly_fields    = ('creation_date', 'last_update', 'n_likes', 'n_dislikes', 'n_views')
    list_display_links = ['title']
    list_filter        = ('creation_date', 'last_update')
    search_fields      = ['title', 'number']

    show_full_result_count = True


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display       = ['title', 'number', 'type', 'volume_id', 'novela', 'creation_date', 'n_likes', 'n_dislikes', 'n_views']
    ordering           = ['title', 'number']
    readonly_fields    = ('creation_date', 'last_update', 'n_likes', 'n_dislikes', 'n_views')
    list_display_links = ['title', 'number']
    list_filter        = ('type', 'creation_date', 'last_update')
    search_fields      = ['title', 'number']

    empty_value_display    = 'Capítulo'
    show_full_result_count = True

    # para list_display[4] mostrar nombre de novela
    def novela(self, obj):
        return obj.volume_id.novel_id

@admin.register(Illustration)
class IllustrationAdmin(admin.ModelAdmin):
    list_display       = ['name', 'picture', 'novela', 'volume_id', 'uploaded_by', 'upload_date']
    ordering           = ['name']
    readonly_fields    = ['upload_date']
    list_display_links = ['name', 'picture']
    list_filter        = ('volume_id', 'uploaded_by', 'upload_date')
    search_fields      = ['name', 'novela', 'volume_id', 'uploaded_by']

    show_full_result_count = True

    # para list_display[2] mostrar nombre de novela
    def novela(self, obj):
        return obj.volume_id.novel_id