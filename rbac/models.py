# _*_ encoding:utf-8 _*_
from django.db import models
from django.contrib.auth.models import AbstractUser

class Menu(models.Model):
    """
    菜单
    """
    title = models.CharField(max_length=32, unique=True,verbose_name=u'菜单')
    parent = models.ForeignKey("Menu", null=True, blank=True,on_delete=models.CASCADE)
    # 定义菜单间的自引用关系
    # 权限url 在 菜单下；菜单可以有父级菜单；还要支持用户创建菜单，因此需要定义parent字段（parent_id）
    # blank=True 意味着在后台管理中填写可以为空，根菜单没有父级菜单

    def __str__(self):
        # 显示层级菜单
        title_list = [self.title]
        p = self.parent
        while p:
            title_list.insert(0, p.title)
            p = p.parent
        return '-'.join(title_list)

    class Meta:
        verbose_name = u"菜单"
        verbose_name_plural = verbose_name


class Permission(models.Model):
    """
    权限
    """
    title = models.CharField(max_length=32, unique=True,verbose_name = u"权限")
    url = models.CharField(max_length=128, unique=True)
    menu = models.ForeignKey("Menu", null=True, blank=True,on_delete=models.CASCADE)

    def __str__(self):
        # 显示带菜单前缀的权限
        return '{menu}---{permission}'.format(menu=self.menu, permission=self.title)

    class Meta:
        verbose_name = u"权限"
        verbose_name_plural = verbose_name


class Role(models.Model):
    """
    角色：绑定权限
    """
    title = models.CharField(max_length=32, unique=True,verbose_name = u"角色")
    permissions = models.ManyToManyField("Permission")
    # 定义角色和权限的多对多关系

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = u"角色"
        verbose_name_plural = verbose_name


class User(models.Model):
    """
    用户：划分角色
    """
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    email = models.EmailField(verbose_name='邮箱')
    roles = models.ManyToManyField(to='Role',verbose_name='角色')

    class Meta:
        verbose_name = u"用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username