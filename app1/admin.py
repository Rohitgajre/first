from django.contrib import admin
# from .models import Person
from .models import *


# Register your models here.
admin.site.register([Person, College, Principle, Department, Student, Subjects])

# first user is called superuser or admin
