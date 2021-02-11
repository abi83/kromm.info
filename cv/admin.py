from django.contrib import admin
from modeltranslation.admin import (
    TranslationAdmin, TabbedTranslationAdmin, TranslationStackedInline, TranslationTabularInline)


from .models import Study, Project, ProjectImage


@admin.register(Study)
class PostAdmin(TranslationAdmin):
    list_display = ('name', )
    empty_value_display = '-пусто-'
    search_fields = ('name',)


class ProjectImageAdmin(TranslationTabularInline):
    model = ProjectImage
    extra = 0


@admin.register(Project)
class ProjectAdmin(TabbedTranslationAdmin):
    list_display = ('title', 'short_desc', 'start_date', 'end_date', 'active')
    inlines = [ProjectImageAdmin, ]
