from django.db import models


# Create your models here.

class ProductModel(models.Model):
    title = models.CharField('Название', max_length=255)
    url = models.URLField('Ссылка на продукт')
    is_active = models.BooleanField('Статус удаления', default=False)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        db_table = 'Product'

    def __str__(self):
        return f'{self.title}'
