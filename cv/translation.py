from modeltranslation.translator import register, TranslationOptions
from .models import Study, Project


@register(Study)
class StudyTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ('title', 'short_desc', 'description',)