from django.contrib import admin
from .models import Fansub, Support, Membership

@admin.register(Fansub)
class FansubAdmin(admin.ModelAdmin):
    list_display       = ['name', 'cover', 'creation_date', 'last_update', 'likes', 'dislikes', 'views']
    ordering           = ['name']
    readonly_fields    = ('creation_date', 'last_update', 'likes', 'dislikes', 'views')
    list_display_links = ['name']
    list_filter        = ('creation_date', 'last_update')
    search_fields      = ['name']
    
    show_full_result_count = True


@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display       = ['fansub', 'user', 'role', 'date_joined']
    ordering           = ['fansub']
    readonly_fields    = ('date_joined', )
    list_display_links = ['fansub', 'user']
    list_filter        = ('date_joined', 'role')
    search_fields      = ['fansub', 'user', 'role']
    
    show_full_result_count = True


@admin.register(Support)
class SupportAdmin(admin.ModelAdmin):
    list_display       = ['fansub', 'chapter', 'last_update', 'views']
    ordering           = ['fansub']
    readonly_fields    = ('creation_date', 'last_update')
    list_display_links = ['fansub', 'chapter']
    list_filter        = ('creation_date', 'last_update')
    search_fields      = ['fansub', 'chapter']
    
    show_full_result_count = True
