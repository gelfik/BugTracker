from django.db import models


# Create your models here.


class BugModel(models.Model):
    product = models.ForeignKey('ProductApp.ProductModel', on_delete=models.CASCADE, verbose_name='Продукт')
    title = models.CharField('Заголовок', max_length=255)
    steps = models.TextField('Шаги воспроизведения')
    actual_result = models.TextField('Фактический результат')
    expected_result = models.TextField('Ожидаемый результат')
    problem_type = models.ForeignKey('StatusApp.ProblemTypeModel', on_delete=models.CASCADE, verbose_name='Проблема',
                                     default=None)
    priority_type = models.ForeignKey('StatusApp.PriorityTypeModel', on_delete=models.CASCADE, verbose_name='Приоритет',
                                      default=None)
    files = models.ManyToManyField('FilesApp.FileModel', verbose_name='Файлы', blank=True)
    is_active = models.BooleanField('Статус удаления', default=False)

    class Meta:
        verbose_name = 'Баг'
        verbose_name_plural = 'Баги'
        db_table = 'Bug'

    def __str__(self):
        return f'{self.title}'
