from django.db import models


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
    title = models.CharField('Projects title', max_length=255)
    short_desc = models.TextField()
    description = models.TextField()
    start_time = models.DateField()
    end_time = models.DateField()


class ProjectImage(models.Model):
    """
    Projects images
    """
    project = models.ForeignKey(Project, blank=False, null=False, on_delete=models.CASCADE, related_name='images', verbose_name='Link to project by ID')
    file = models.ImageField(upload_to='project_images/', blank=False, null=False, verbose_name='Image file link')
    cover = models.BooleanField(default=False)
