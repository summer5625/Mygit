# Generated by Django 3.0.3 on 2020-02-11 06:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=32, verbose_name='部门')),
            ],
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('hostname', models.CharField(max_length=64, verbose_name='主机名')),
                ('ip', models.CharField(max_length=128, verbose_name='IP')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=32, verbose_name='角色名称')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32, verbose_name='用户名')),
                ('gender', models.IntegerField(choices=[(1, '男'), (2, '女')], default=1, verbose_name='性别')),
                ('password', models.CharField(max_length=64, verbose_name='密码')),
                ('email', models.CharField(max_length=32, verbose_name='邮箱')),
                ('depart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web1.Department', verbose_name='部门')),
            ],
        ),
    ]
