from django.db import models


# Create your models here.

class FileModel(models.Model):
    def get_file_path(instance, filename):
        import os
        return os.path.join('', filename)

    file = models.FileField(upload_to=get_file_path, verbose_name='Файл', default=None, null=True)

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'
        db_table = 'File'

    def __str__(self):
        return self.file.url
