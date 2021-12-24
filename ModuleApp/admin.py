from django.contrib import admin

# Register your models here.
from ModuleApp.models import ModuleModel, SubSystemModel
from ProductApp.models import ProductModel


class ProductFilter(admin.SimpleListFilter):
    title = 'Продукт'
    parameter_name = 'product'

    def lookups(self, request, model_admin):
        chapters = set([c.product for c in model_admin.model.objects.all()])
        return [(b.id, f'{b.title}') for b in chapters]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(product__id__exact=self.value())


class ProductForModuleFilter(admin.SimpleListFilter):
    title = 'Продукт'
    parameter_name = 'product'

    def lookups(self, request, model_admin):
        chapters = set(
            [c for c in ProductModel.objects.filter(subsystemmodel__modules__in=model_admin.model.objects.all())])
        return [(b.id, f'{b.title}') for b in chapters]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(subsystemmodel__product__id__exact=self.value())


class SubSystemFilter(admin.SimpleListFilter):
    title = 'Подсистема'
    parameter_name = 'subsystem'

    def lookups(self, request, model_admin):
        product = request.GET.get('product', None)
        if product:
            chapters = set([c for c in SubSystemModel.objects.filter(product_id=product)])
        else:
            chapters = set([c for c in SubSystemModel.objects.all()])
        return [(b.id, f'{b.title}') for b in chapters]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(subsystemmodel__id__exact=self.value())


class BugsInline(admin.TabularInline):
    model = ModuleModel.bugs.through
    extra = 0
    verbose_name = 'Баг'
    verbose_name_plural = 'Баги'


class ModulesInline(admin.TabularInline):
    model = SubSystemModel.modules.through
    extra = 0
    verbose_name = 'Модуль'
    verbose_name_plural = 'Модули'


@admin.register(ModuleModel)
class ModuleListAdmin(admin.ModelAdmin):
    list_display = ('title', 'status_type', 'id',)
    search_fields = ['title', ]
    list_filter = (ProductForModuleFilter, SubSystemFilter, 'status_type',)
    readonly_fields = ('bugs',)
    inlines = [BugsInline]

    # autocomplete_fields = ['bugs']

    fieldsets = (
        (None, {
            'fields': (
                'title', 'status_type', 'description',)
        }),
        ('Баги', {
            'classes': ('collapse',),
            'fields': ('bugs',),
        }),
    )


@admin.register(SubSystemModel)
class SubSystemListAdmin(admin.ModelAdmin):
    list_display = ('product', 'title', 'status_type', 'id',)
    search_fields = ['title', ]
    list_filter = (ProductFilter, 'status_type',)
    readonly_fields = ('modules',)
    inlines = [ModulesInline]
    # radio_fields = {"status_type": admin.VERTICAL}

    fieldsets = (
        (None, {
            'fields': (
                'product', 'title', 'status_type', 'description',)
        }),
        ('Модули', {
            'classes': ('collapse',),
            'fields': ('modules',),
        }),
    )
