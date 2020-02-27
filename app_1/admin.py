from django.contrib import admin

# Register your models here.
from .models import blogpost,shopProduct

admin.site.register(blogpost )
admin.site.register(shopProduct )
