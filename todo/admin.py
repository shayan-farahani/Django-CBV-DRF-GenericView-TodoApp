from django.contrib import admin
from .models import Task
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ["title", "complete"]
    fields = ["title", "complete"]
    list_filter = ("title",)


admin.site.register(Task, TaskAdmin)