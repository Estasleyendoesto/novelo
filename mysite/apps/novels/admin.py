from django.contrib import admin
from .models import Novel, Distro, Chapter, Illustration

@admin.register(Novel)
class NovelAdmin(admin.ModelAdmin):
    list_display       = ['title', 'type', 'structure', 'last_update', 'likes', 'dislikes', 'views']
    ordering           = ['title']
    readonly_fields    = ('creation_date', 'last_update', 'likes', 'dislikes', 'views')
    list_display_links = ['title']
    list_filter        = ('type', 'structure', 'creation_date')
    search_fields      = ['title']
    
    show_full_result_count = True


@admin.register(Distro)
class DistroAdmin(admin.ModelAdmin):
    list_display       = ['title', 'numero', 'novel', 'creation_date', 'last_update', 'likes', 'dislikes', 'views']
    ordering           = ['title', 'numero']
    readonly_fields    = ('creation_date', 'last_update', 'likes', 'dislikes', 'views')
    list_display_links = ['title']
    list_filter        = ('creation_date', 'last_update')
    search_fields      = ['title', 'numero']

    show_full_result_count = True


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display       = ['title', 'numero', 'type', 'distro', 'novela', 'creation_date']
    ordering           = ['title', 'numero']
    readonly_fields    = ('creation_date', 'last_update')
    list_display_links = ['title', 'numero']
    list_filter        = ('type', 'creation_date', 'last_update')
    search_fields      = ['title', 'numero']

    empty_value_display    = '---'
    show_full_result_count = True

    # para list_display[4] mostrar nombre de novela
    def novela(self, obj):
        return obj.distro.novel

@admin.register(Illustration)
class IllustrationAdmin(admin.ModelAdmin):
    list_display       = ['name', 'picture', 'novela', 'distro', 'uploaded_by', 'upload_date']
    ordering           = ['name']
    readonly_fields    = ['upload_date']
    list_display_links = ['name', 'picture']
    list_filter        = ('distro', 'uploaded_by', 'upload_date')
    search_fields      = ['name', 'novela', 'distro', 'uploaded_by']

    show_full_result_count = True

    # para list_display[2] mostrar nombre de novela
    def novela(self, obj):
        return obj.distro.novel