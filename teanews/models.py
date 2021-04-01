from django.db import models

# Create your models here.

class Article(models.Model):

    title = models.CharField(max_length=150)
    preview = models.CharField(max_length=250)
    full_text = models.TextField()
    created_at = models.DateTimeField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новина'
        verbose_name_plural = 'Новини'
