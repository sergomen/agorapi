from django.contrib import admin

# Register your models here.
from .models import Advocate, Company

admin.site.register(Advocate)
admin.site.register(Company)
