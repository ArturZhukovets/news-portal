from django.db import models


class NewsArticles(models.Model):
    title = models.CharField(max_length=50)
    anons = models.CharField(verbose_name='preview', max_length=250, default='')
    full_text = models.TextField()
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:               # display model in admin panel
        verbose_name_plural = "NEWS"

