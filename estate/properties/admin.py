from django.contrib import admin
from .models import Properties,Property_type,Status
# Register your models here.
admin.site.register(Properties)
admin.site.register(Property_type)
admin.site.register(Status)