from django.db import models
from .utils import from_cyrillic_to_eng


# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название города', unique=True)
    slug = models.CharField(max_length=50, blank=True, unique=True)

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(str(self.name))
        super().save(*args, **kwargs)


class Language(models.Model):
    name = models.CharField(max_length=50, verbose_name='Язык програмирования', unique=True)
    slug = models.CharField(max_length=50, blank=True, unique=True)

    class Meta:
        # Имя приложения(класса) на русском
        verbose_name = 'Язык програмирования'
        # Множественное число
        verbose_name_plural = 'Языки програмирования'

    def __str__(self):
        # переопределяем название объекта на  точто в name = models.CharField
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(str(self.name))
        super().save(*args, **kwargs)


class Vacancy(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField(max_length=250, verbose_name='Название вакансии')
    company = models.CharField(max_length=200, verbose_name='Компании')
    description = models.TextField(verbose_name='Описание вакансии')
    city = models.ForeignKey('City', on_delete=models.CASCADE, verbose_name='Город')
    language = models.ForeignKey('Language', on_delete=models.CASCADE, verbose_name='Язык программирования')
    timestamp = models.DateField(auto_now_add=True)

    class Meta:
        # Имя приложения(класса) на русском
        verbose_name = 'Вакансия'
        # Множественное число
        verbose_name_plural = 'Вакансии'

    def __str__(self):
        # переопределяем название объекта на  точто в name = models.CharField
        return self.title
