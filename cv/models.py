from django.db import models
from sorl.thumbnail import ImageField
from tinymce.models import HTMLField


class Study(models.Model):
    """
    Universities etc.
    """
    name = models.CharField("Учеба", max_length=150)

    class Meta:
        verbose_name = "Учеба"
        verbose_name_plural = "Учебы"


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


class ProjectImage(models.Model):
    """
    Projects images
    """
    project = models.ForeignKey(Project, blank=False, null=False, on_delete=models.CASCADE, related_name='images', verbose_name='Link to project by ID')
    file = ImageField(upload_to='project_images/', blank=False, null=False, verbose_name='Image file link')
    cover = models.BooleanField(default=False)
    title = models.CharField(max_length=125, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
