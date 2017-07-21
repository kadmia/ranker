from django.contrib import admin

from .models import RankEntity, RankParent, Author, GameState, Genre


@admin.register(RankParent)
class RankParentAdmin(admin.ModelAdmin):
    fields = (('name', 'slug'), ('show_in_navbar', 'active'), 'description', ('internal_creation_datetime', 'internal_last_modified_datetime'))
    readonly_fields = ('internal_creation_datetime', 'internal_last_modified_datetime')
    list_display = ('name', 'show_in_navbar', 'active', 'internal_creation_datetime', 'internal_last_modified_datetime')


@admin.register(RankEntity)
class RankEntityAdmin(admin.ModelAdmin):
    fields = (('name', 'slug'),
              'description',
              ('created', 'last_update'),
              ('game_state', 'genre'),
              'authors',
              'website',
              'source_url' ,
              'documentation_url',
              'license_type',
              'active',
              'votes',
              'parent',
              ('internal_creation_datetime', 'internal_last_modified_datetime'))
    readonly_fields = ('internal_creation_datetime', 'internal_last_modified_datetime', 'votes')
    list_display = ('name', 'votes', 'internal_creation_datetime', 'internal_last_modified_datetime')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(GameState)
class GameStateAdmin(admin.ModelAdmin):
    pass


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass
