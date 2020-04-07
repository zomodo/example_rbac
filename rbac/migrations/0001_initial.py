# Generated by Django 2.2.11 on 2020-04-02 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='操作名称')),
                ('code', models.CharField(max_length=32, verbose_name='操作码')),
            ],
            options={
                'verbose_name_plural': '操作信息',
                'verbose_name': '操作信息',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='菜单标题')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rbac.Menu', verbose_name='父菜单')),
            ],
            options={
                'verbose_name_plural': '菜单信息',
                'verbose_name': '菜单信息',
            },
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='权限名称')),
                ('url', models.CharField(max_length=32, verbose_name='权限链接')),
                ('menu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='rbac.Menu', verbose_name='权限菜单')),
            ],
            options={
                'verbose_name_plural': '权限信息',
                'verbose_name': '权限信息',
            },
        ),
        migrations.CreateModel(
            name='Permission2Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rbac.Action', verbose_name='操作名称')),
                ('permission', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rbac.Permission', verbose_name='权限名称')),
            ],
            options={
                'verbose_name_plural': '权限详细操作',
                'verbose_name': '权限详细操作',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='角色名称')),
            ],
            options={
                'verbose_name_plural': '角色信息',
                'verbose_name': '角色信息',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, verbose_name='账户名称')),
                ('password', models.CharField(max_length=32, verbose_name='账户密码')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
            ],
            options={
                'verbose_name_plural': '用户信息',
                'verbose_name': '用户信息',
            },
        ),
        migrations.CreateModel(
            name='User2Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rbac.Role', verbose_name='账户角色')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rbac.User', verbose_name='账户名称')),
            ],
            options={
                'verbose_name_plural': '账户角色信息',
                'verbose_name': '账户角色信息',
            },
        ),
        migrations.CreateModel(
            name='Permission2Action2Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p2a', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rbac.Permission2Action', verbose_name='权限详细操作')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rbac.Role', verbose_name='角色名称')),
            ],
            options={
                'verbose_name_plural': '角色的权限详细操作',
                'verbose_name': '角色的权限详细操作',
            },
        ),
    ]
