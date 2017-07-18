from django.contrib import admin

from .models import RankEntity, RankParent


@admin.register(RankParent)
class RankParentAdmin(admin.ModelAdmin):
    fields = ('name', 'slug', 'show_in_navbar', 'active', 'description',('creation_datetime', 'last_modified_datetime'))
    readonly_fields = ('creation_datetime', 'last_modified_datetime')
    list_display = ('name', 'show_in_navbar', 'active', 'creation_datetime', 'last_modified_datetime')


@admin.register(RankEntity)
class RankEntityAdmin(admin.ModelAdmin):
    fields = ('name', 'slug', 'description', 'parent', 'votes', ('creation_datetime', 'last_modified_datetime'))
    readonly_fields = ('creation_datetime', 'last_modified_datetime', 'votes')
    list_display = ('name', 'votes', 'creation_datetime', 'last_modified_datetime')

