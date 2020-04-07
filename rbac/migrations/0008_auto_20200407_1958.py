# Generated by Django 2.2.11 on 2020-04-07 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0007_auto_20200407_1741'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menu',
            options={'verbose_name': '菜单', 'verbose_name_plural': '菜单'},
        ),
        migrations.AlterModelOptions(
            name='permission',
            options={'verbose_name': '权限', 'verbose_name_plural': '权限'},
        ),
        migrations.AlterModelOptions(
            name='role',
            options={'verbose_name': '角色', 'verbose_name_plural': '角色'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '用户', 'verbose_name_plural': '用户'},
        ),
        migrations.RemoveField(
            model_name='permission',
            name='code',
        ),
        migrations.RemoveField(
            model_name='permission',
            name='group',
        ),
        migrations.RemoveField(
            model_name='permission',
            name='menu_gp',
        ),
        migrations.AddField(
            model_name='menu',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rbac.Menu'),
        ),
        migrations.AddField(
            model_name='permission',
            name='menu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rbac.Menu'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='title',
            field=models.CharField(max_length=32, unique=True, verbose_name='菜单'),
        ),
        migrations.AlterField(
            model_name='permission',
            name='title',
            field=models.CharField(max_length=32, unique=True, verbose_name='权限'),
        ),
        migrations.AlterField(
            model_name='permission',
            name='url',
            field=models.CharField(max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='role',
            name='permissions',
            field=models.ManyToManyField(to='rbac.Permission'),
        ),
        migrations.AlterField(
            model_name='role',
            name='title',
            field=models.CharField(max_length=32, unique=True, verbose_name='角色'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='邮箱'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='user',
            name='roles',
            field=models.ManyToManyField(to='rbac.Role', verbose_name='角色'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=32),
        ),
        migrations.DeleteModel(
            name='Group',
        ),
    ]