from django.contrib import admin
from .models import services
# Register your models here.
class serviceadmin(admin.ModelAdmin):
    list_display = ('Name','area_of_site','Your_dream_building')

admin.site.register(services,serviceadmin)