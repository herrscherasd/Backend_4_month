from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=300, verbose_name="Заголовок записи")
    content = models.TextField(verbose_name="Содержание записи")
    status = models.BooleanField(default=True, verbose_name="Статус публикации")
    created = models.DateTimeField(auto_now=True, verbose_name="Дата создания")


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"