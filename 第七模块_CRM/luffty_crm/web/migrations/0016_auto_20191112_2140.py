# Generated by Django 2.0.1 on 2019-11-12 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0015_auto_20191112_2028'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScoreRecord',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField(verbose_name='理由')),
                ('score', models.IntegerField(help_text='违纪扣分写负值，表现邮寄加分写正值', verbose_name='分值')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='score',
            field=models.IntegerField(default=100, verbose_name='积分'),
        ),
        migrations.AddField(
            model_name='scorerecord',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Student', verbose_name='学生'),
        ),
        migrations.AddField(
            model_name='scorerecord',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.UserInfo', verbose_name='执行人'),
        ),
    ]
