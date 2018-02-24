from django.contrib import admin

# Register your models here.
from taller1.microservicio1.models import *

admin.site.register(Category)
admin.site.register(Provider)