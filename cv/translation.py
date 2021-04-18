from modeltranslation.translator import register, TranslationOptions
from .models import Study, Job, Project, ProjectImage, CV


@register(Study)
class StudyTranslationOptions(TranslationOptions):
    fields = ('name', 'degree', 'description',)


@register(Job)
class JobTranslationOptions(TranslationOptions):
    fields = ('name', 'position', 'description', )


@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ('title', 'short_desc', 'description', )


@register(ProjectImage)
class ProjectImageTranslationOptions(TranslationOptions):
    fields = ('title', 'description', )


@register(CV)
class CVTranslationOptions(TranslationOptions):
    fields = ('position', )
