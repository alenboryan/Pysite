from django.contrib import admin

from .models import PyUser
from .models import Info

admin.site.register(PyUser),
admin.site.register(Info)
