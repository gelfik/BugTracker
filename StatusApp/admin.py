from django.contrib import admin

# Register your models here.
from StatusApp.models import (PriorityTypeModel, ProblemTypeModel, StatusTypeModel)


@admin.register(PriorityTypeModel)
class PriorityTypeListAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'key',)


@admin.register(ProblemTypeModel)
class ProblemTypeListAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'key',)


@admin.register(StatusTypeModel)
class StatusTypeListAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'key',)
