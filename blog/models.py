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

class Comment(models.Model):
    username = models.CharField(max_length=16, verbose_name="Имя пользователя")
    text = models.CharField(max_length=300, verbose_name="Комментарий")
    created = models.DateTimeField(auto_now=True, verbose_name="Дата создания комментария")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_comment", verbose_name="Пост")

    def __str__(self):
        return f"{self.username} - {self.post.title}"
    
    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Коментарии"