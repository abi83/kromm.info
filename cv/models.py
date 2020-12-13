from django.db import models


class Study(models.Model):
    """Учеба"""
    name = models.CharField("Учеба", max_length=150)

    class Meta:
        verbose_name = "Учеба"
        verbose_name_plural = "Учебы"