from django.db import models


class Study(models.Model):
    """Учеба"""
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
    start_time = models.TimeField()
    end_time = models.TimeField()