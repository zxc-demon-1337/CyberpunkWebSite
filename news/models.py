from django.db import models

class Articles(models.Model):
    title = models.CharField('Название', max_length=50, default='Пенес')
    anons = models.CharField('Анонс', max_length=250, default='Пенесяка')
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата и время')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
