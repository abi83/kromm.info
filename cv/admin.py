from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TabbedTranslationAdmin


from .models import Study, Project, ProjectImage


@admin.register(Study)
class PostAdmin(TranslationAdmin):
    list_display = ('name', )
    empty_value_display = '-пусто-'
    search_fields = ('name',)


class ProjectImageAdmin(admin.StackedInline):
    model = ProjectImage


@admin.register(Project)
class ProjectAdmin(TabbedTranslationAdmin):
    list_display = ('title', 'short_desc', 'start_time', 'end_time')
    inlines = [ProjectImageAdmin, ]