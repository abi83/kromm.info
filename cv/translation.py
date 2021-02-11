from modeltranslation.translator import register, TranslationOptions
from .models import Study, Project, ProjectImage


@register(Study)
class StudyTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ('title', 'short_desc', 'description', )


@register(ProjectImage)
class ProjectImageTranslationOptions(TranslationOptions):
    fields = ('title', 'description', )
