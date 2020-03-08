from django.contrib import admin
from . import models


class StepInline(admin.TabularInline):
    model = models.Step

@admin.register(models.Tutorial)
class TutorialAdmin(admin.ModelAdmin):
    inlines = [StepInline]

    list_display = ('title', )
    
    prepopulated_fields = {'slug': ('title',)}
