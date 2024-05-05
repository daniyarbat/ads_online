from django.conf import settings
from django.db import models

NULLABLE = {
    "null": True,
    "blank": True
}


class Ad(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    price = models.PositiveIntegerField(default=0, verbose_name='цена')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    image = models.ImageField(upload_to='media', **NULLABLE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="пользователь", **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="время создания")

    def __str__(self):
        return f"{self.title} - {self.price}"

    class Meta:
        verbose_name = "объявление"
        verbose_name_plural = "объявления"
        ordering = ["-created_at"]


class Comment(models.Model):
    text = models.TextField(verbose_name="текст отзыва")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="пользователь", **NULLABLE)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, verbose_name="объявление")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="время создания")

    def __str__(self):
        return f"{self.ad}: {self.text}"

    class Meta:
        verbose_name = "отзыв"
        verbose_name_plural = "отзывы"
