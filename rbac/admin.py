from django.contrib import admin
from rbac import models
from .AdminForm import AdminPermissionForm

# Register your models here.
admin.site.register(models.User)
admin.site.register(models.Menu)
admin.site.register(models.Role)
admin.site.register(models.Action)

@admin.register(models.Permission)
class PermissionAdmin(admin.ModelAdmin):
    form=AdminPermissionForm

    def action_show(self,obj):
        return [act.title for act in obj.action.all()]

    list_display = ('title','url','action_show','menu')









