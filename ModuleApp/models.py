from django.db import models

from django.contrib.auth.models import User


# Create your models here.


class ModuleModel(models.Model):
    title = models.CharField('Подмодуль', max_length=255)
    status_type = models.ForeignKey('StatusApp.StatusTypeModel', on_delete=models.CASCADE, verbose_name='Статус',
                                    default=None)
    description = models.TextField('Комментарий', blank=True, null=True)
    bugs = models.ManyToManyField('BugApp.BugModel', verbose_name='Баги', blank=True)
    is_active = models.BooleanField('Статус удаления', default=False)

    class Meta:
        verbose_name = 'Модуль'
        verbose_name_plural = 'Модули'
        db_table = 'Module'

    def __str__(self):
        return f'{self.title}'


class SubSystemModel(models.Model):
    product = models.ForeignKey('ProductApp.ProductModel', on_delete=models.CASCADE, verbose_name='Продукт')
    title = models.CharField('Подсистема', max_length=255)
    status_type = models.ForeignKey('StatusApp.StatusTypeModel', on_delete=models.CASCADE, verbose_name='Статус',
                                    default=None)
    description = models.TextField('Комментарий', blank=True, null=True)
    modules = models.ManyToManyField('ModuleApp.ModuleModel', verbose_name='Модули', blank=True)
    is_active = models.BooleanField('Статус удаления', default=False)

    class Meta:
        verbose_name = 'Подсистема'
        verbose_name_plural = 'Подсистемы'
        db_table = 'SubSystem'

    def __str__(self):
        return f'{self.title}'
