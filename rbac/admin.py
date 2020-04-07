from django.contrib import admin
from rbac import models

# Register your models here.
admin.site.register(models.User)
admin.site.register(models.Menu)
admin.site.register(models.Role)
admin.site.register(models.Permission)








