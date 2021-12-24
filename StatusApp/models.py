from django.db import models


# Create your models here.

class PriorityTypeModel(models.Model):
    title = models.CharField('Название', max_length=255)
    key = models.CharField('Ключ', max_length=255, unique=True)

    class Meta:
        verbose_name = 'Тип приоритета'
        verbose_name_plural = 'Типы приоритета'
        db_table = 'PriorityType'

    def __str__(self):
        return f'{self.title}'


class ProblemTypeModel(models.Model):
    title = models.CharField('Название', max_length=255)
    key = models.CharField('Ключ', max_length=255, unique=True)

    class Meta:
        verbose_name = 'Тип проблемы'
        verbose_name_plural = 'Типы проблем'
        db_table = 'ProblemType'

    def __str__(self):
        return f'{self.title}'


class StatusTypeModel(models.Model):
    title = models.CharField('Название', max_length=255)
    key = models.CharField('Ключ', max_length=255, unique=True)

    class Meta:
        verbose_name = 'Тип статуса'
        verbose_name_plural = 'Типы статусов'
        db_table = 'StatusType'

    def __str__(self):
        return f'{self.title}'
