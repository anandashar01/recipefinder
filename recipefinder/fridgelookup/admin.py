from django.contrib import admin

from .models import Recipe, Fridge

class FridgeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['fridge_name', 'ingredients']})
    ]
admin.site.register(Fridge, FridgeAdmin)
admin.site.register(Recipe)