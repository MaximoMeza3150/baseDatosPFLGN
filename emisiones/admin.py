from django.contrib import admin
from .models import Emision

class EmisionAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)

# Register your models here.
admin.site.register(Emision, EmisionAdmin)
