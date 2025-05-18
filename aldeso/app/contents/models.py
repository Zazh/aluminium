# contents/models.py
from django.db import models


class HomePage(models.Model):
    title = models.CharField("Заголовок", max_length=255)
    subtitle = models.CharField("Подзаголовок", max_length=255, blank=True)
    seo_title = models.CharField("SEO Title", max_length=255, blank=True)
    seo_description = models.TextField("SEO Description", blank=True)

    def __str__(self):
        return "Главная страница"

    class Meta:
        verbose_name = "Главная страница"
        verbose_name_plural = "Главная страница"


class Contact(models.Model):
    name = models.CharField("Название контакта", max_length=100)
    value = models.CharField("Значение", max_length=255)
    link = models.CharField("Ссылка", max_length=255, default="Nulle")
    order = models.PositiveIntegerField(default=0)  # Новое поле для порядка

    def __str__(self):
        return f"{self.name}: {self.value}"

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
        ordering = ["order", "name"]

class FooterLink(models.Model):
    name = models.CharField("Название ссылки", max_length=100)
    url = models.URLField("URL ссылки")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ссылка в футере"
        verbose_name_plural = "Ссылки в футере"