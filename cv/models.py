from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from sorl.thumbnail import ImageField
from tinymce.models import HTMLField


class Study(models.Model):
    """
    Universities etc.
    """
    name = models.CharField(_('Учеба'), max_length=150)
    degree = models.TextField()
    description = HTMLField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('start_date', )
        verbose_name = _('Учеба')
        verbose_name_plural = _('Учебы')


class Job(models.Model):
    """
    Places I worked
    """
    name = models.CharField(_('Работа'), max_length=150)
    position = models.TextField()
    description = HTMLField()
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        verbose_name = _('Работа')
        verbose_name_plural = _('Работы')
        ordering = ('-end_date', )

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(_('Скилл'), max_length=25)
    rank = models.CharField(_('Опыт'), max_length=25)
    description = models.CharField(_('Описание'), max_length=127)

    class Meta:
        ordering = ('-rank', )

    def __str__(self):
        return self.name


class Project(models.Model):
    """
    Projects done
    """
    active = models.BooleanField(default=True)
    title = models.CharField('Projects title', max_length=255)
    short_desc = models.TextField()
    description = HTMLField()
    start_date = models.DateField()
    end_date = models.DateField()
    role = models.CharField(max_length=125, null=True, blank=True)
    url = models.URLField(null=True, blank=True)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('project-detail', args=[str(self.id)])

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    """
    Projects images
    """
    project = models.ForeignKey(Project, blank=False, null=False, on_delete=models.CASCADE, related_name='images', verbose_name='Link to project by ID')
    file = ImageField(upload_to='project_images/', blank=False, null=False, verbose_name='Image file link')
    cover = models.BooleanField(default=False)
    title = models.CharField(max_length=125, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)


class CV(models.Model):
    """
    A class representing one CV
    """
    slug = models.SlugField(unique=True, max_length=25, verbose_name=_('URL слаг'))
    position = models.CharField(_('Должность'), max_length=50)
    text = models.TextField(blank=True)
    jobs = models.ManyToManyField(Job, verbose_name=_('Опыт работы'))
    education = models.ManyToManyField(Study, verbose_name=_('Образование'))
    skills = models.ManyToManyField(Skill, verbose_name=_('Скиллы'))
    projects = models.ManyToManyField(Project, verbose_name=_('Мои проекты'))

    def __str__(self):
        return self.position


class Cover(models.Model):
    """
    Cover letter
    """
    active = models.BooleanField(default=True)
    company = models.CharField('To company', max_length=255)
    to = models.CharField('To person', default='Hiring Manager', max_length=255)
    date = models.DateField()
    position = models.CharField(max_length=125, null=True, blank=True)
    description = HTMLField()

    def __str__(self):
        return f' to{self.company} at {self.position}'
