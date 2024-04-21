from django.contrib import admin
from .models import CustomUser, Company, File, Folder

admin.site.register(CustomUser)
admin.site.register(Company)
admin.site.register(File)
admin.site.register(Folder)
