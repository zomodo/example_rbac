# Generated by Django 2.2.11 on 2020-04-07 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0004_auto_20200403_1225'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=32, verbose_name='组名称')),
            ],
            options={
                'verbose_name_plural': 'Group组表',
            },
        ),
        migrations.RemoveField(
            model_name='permission2action',
            name='action',
        ),
        migrations.RemoveField(
            model_name='permission2action',
            name='permission',
        ),
        migrations.RemoveField(
            model_name='permission2action2role',
            name='p2a',
        ),
        migrations.RemoveField(
            model_name='permission2action2role',
            name='role',
        ),
        migrations.RemoveField(
            model_name='user2role',
            name='role',
        ),
        migrations.RemoveField(
            model_name='user2role',
            name='user',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='permission',
            name='menu',
        ),
        migrations.AddField(
            model_name='permission',
            name='code',
            field=models.CharField(default=0, max_length=32, verbose_name='url代码'),
        ),
        migrations.AddField(
            model_name='permission',
            name='is_menu',
            field=models.BooleanField(default=True, verbose_name='是否是菜单'),
        ),
        migrations.AddField(
            model_name='role',
            name='permissions',
            field=models.ManyToManyField(blank=True, to='rbac.Permission', verbose_name='具有的所有权限'),
        ),
        migrations.AddField(
            model_name='user',
            name='roles',
            field=models.ManyToManyField(blank=True, to='rbac.Role', verbose_name='具有的所有角色'),
        ),
        migrations.DeleteModel(
            name='Action',
        ),
        migrations.DeleteModel(
            name='Permission2Action',
        ),
        migrations.DeleteModel(
            name='Permission2Action2Role',
        ),
        migrations.DeleteModel(
            name='User2Role',
        ),
        migrations.AddField(
            model_name='group',
            name='menu',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='rbac.Menu', verbose_name='组所属菜单'),
        ),
        migrations.AddField(
            model_name='permission',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='rbac.Group', verbose_name='所属组'),
        ),
    ]
