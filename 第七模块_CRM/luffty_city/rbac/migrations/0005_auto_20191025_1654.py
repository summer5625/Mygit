# Generated by Django 2.0.1 on 2019-10-25 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0004_permission_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('mid', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=32, null=True, verbose_name='一级菜单名称')),
                ('icon', models.CharField(blank=True, max_length=64, null=True, verbose_name='图标')),
            ],
        ),
        migrations.RemoveField(
            model_name='permission',
            name='icon',
        ),
        migrations.RemoveField(
            model_name='permission',
            name='is_menu',
        ),
        migrations.AddField(
            model_name='permission',
            name='menu',
            field=models.ForeignKey(blank=True, help_text='null表示不是菜单;非null表示二级菜单', null=True, on_delete=django.db.models.deletion.CASCADE, to='rbac.Menu', verbose_name='所属菜单'),
        ),
    ]
