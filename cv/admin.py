from django.contrib import admin
from modeltranslation.admin import TranslationAdmin


from .models import Study


@admin.register(Study)
class PostAdmin(TranslationAdmin):
    list_display = ('name', )
    empty_value_display = '-пусто-'
    search_fields = ('name',)
    # list_filter = ('pub_date',)