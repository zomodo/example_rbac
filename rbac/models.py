# _*_ encoding:utf-8 _*_
from django.db import models

class Menu(models.Model):
    """
    菜单
    """
    title = models.CharField(max_length=32,verbose_name='菜单标题')
    parent = models.ForeignKey("Menu", null=True, blank=True,on_delete=models.CASCADE,verbose_name='父菜单')
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
        verbose_name = "菜单信息"
        verbose_name_plural = verbose_name


class Action(models.Model):
    """
    动作
    """
    title=models.CharField(max_length=20,verbose_name='操作名称')
    code=models.CharField(max_length=10,verbose_name='code')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "操作动作"
        verbose_name_plural=verbose_name


class Permission(models.Model):
    """
    权限
    """
    title = models.CharField(max_length=32,verbose_name = '链接标题')
    url = models.CharField(max_length=128,verbose_name='链接URL')
    action = models.ManyToManyField("Action",verbose_name='操作动作')
    menu = models.ForeignKey("Menu", null=True, blank=True,on_delete=models.CASCADE,verbose_name='附属菜单')

    def __str__(self):
        # 显示带菜单前缀的权限
        return '{menu}--{title}--{action}'.format(menu=self.menu, title=self.title,action=[i.title for i in self.action.all()])

    class Meta:
        verbose_name = "权限信息"
        verbose_name_plural = verbose_name


class Role(models.Model):
    """
    角色：绑定权限
    """
    title = models.CharField(max_length=32, unique=True,verbose_name='角色名称')
    permissions = models.ManyToManyField("Permission",verbose_name='角色权限')
    # 定义角色和权限的多对多关系

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "角色信息"
        verbose_name_plural = verbose_name


class User(models.Model):
    """
    用户：划分角色
    """
    username = models.CharField(max_length=32,verbose_name='账户名称')
    password = models.CharField(max_length=64,verbose_name='账户密码')
    email = models.EmailField(verbose_name='邮箱')
    roles = models.ManyToManyField("Role",verbose_name='分配角色')

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username