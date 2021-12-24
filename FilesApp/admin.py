from django.contrib import admin

# Register your models here.
from FilesApp.models import FileModel


@admin.register(FileModel)
class FileListAdmin(admin.ModelAdmin):
    list_display = ('id', 'file',)

    def has_module_permission(self, request):
        return False