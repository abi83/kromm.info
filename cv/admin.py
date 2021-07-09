from django.contrib import admin
from modeltranslation.admin import (
    TranslationAdmin, TabbedTranslationAdmin, TranslationStackedInline, TranslationTabularInline)


from .models import Study, Project, ProjectImage, CV, Skill, Job, Cover


@admin.register(Study)
class StudyAdmin(TabbedTranslationAdmin):
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


@admin.register(CV)
class CVAdmin(TabbedTranslationAdmin):
    pass


@admin.register(Cover)
class CoverAdmin(admin.ModelAdmin):
    pass


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    pass


@admin.register(Job)
class JobAdmin(TabbedTranslationAdmin):
    pass
