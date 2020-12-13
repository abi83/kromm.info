from modeltranslation.translator import register, TranslationOptions
from .models import Study


@register(Study)
class StudyTranslationOptions(TranslationOptions):
    fields = ('name',)