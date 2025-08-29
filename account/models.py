from django.db import models

# Create your models here.

class Image(models.Model):
    # name = models.CharField()
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, default=2)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='products/')
    description = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Картинку'
        verbose_name_plural = 'Картинки'