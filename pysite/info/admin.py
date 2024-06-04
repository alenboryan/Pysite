from django.contrib import admin

from .models import PyUser
from .models import Info, Question, Choice, Pysintax, DjangoInfo, Studying, FlaskInfo


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
    
    
admin.site.register(PyUser),
admin.site.register(Info)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Pysintax)
admin.site.register(DjangoInfo)
admin.site.register(Studying)
admin.site.register(FlaskInfo)