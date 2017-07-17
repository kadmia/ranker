from django.contrib import admin

# Register your models here.

from .models import RankEntity, RankParent

admin.site.register(RankParent)
admin.site.register(RankEntity)
