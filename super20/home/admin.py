from django.contrib import admin
from inspect import ismethoddescriptor
from django.contrib import admin
from home.models import Register
from home.models import Feedback

# Register your models here.
admin.site.register(Register) 
admin.site.register(Feedback) 



