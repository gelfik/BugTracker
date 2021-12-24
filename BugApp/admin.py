from django.contrib import admin

# Register your models here.
from BugApp.models import BugModel


class ProductFilter(admin.SimpleListFilter):
    title = 'Продукт'
    parameter_name = 'product'

    def lookups(self, request, model_admin):
        chapters = set([c.product for c in model_admin.model.objects.all()])
        return [(b.id, f'{b.title}') for b in chapters]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(product__id__exact=self.value())


class FilesInline(admin.TabularInline):
    model = BugModel.files.through
    extra = 0
    verbose_name = 'Файл'
    verbose_name_plural = 'Файлы'


@admin.register(BugModel)
class BugListAdmin(admin.ModelAdmin):
    list_display = ('title', 'product', 'priority_type', 'id',)
    search_fields = ['title', ]
    list_filter = (ProductFilter, 'priority_type', 'problem_type',)
    readonly_fields = ('files',)
    inlines = [FilesInline]

    fieldsets = (
        (None, {
            'fields': (
                'product', 'title', 'steps', 'actual_result', 'expected_result', 'problem_type',
                'priority_type',)
        }),
        ('Ссылки на файлы', {
            'classes': ('collapse',),
            'fields': ('files',),
        }),
    )
