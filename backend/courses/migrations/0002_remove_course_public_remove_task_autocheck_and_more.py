# Generated by Django 5.0.2 on 2024-03-03 15:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='public',
        ),
        migrations.RemoveField(
            model_name='task',
            name='autocheck',
        ),
        migrations.RemoveField(
            model_name='task',
            name='samples',
        ),
        migrations.RemoveField(
            model_name='task',
            name='stdin',
        ),
        migrations.RemoveField(
            model_name='task',
            name='stdout',
        ),
        migrations.RemoveField(
            model_name='task',
            name='tests',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='deadline',
        ),
        migrations.AddField(
            model_name='course',
            name='state',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Черновик'), (1, 'Опубликован')], default=0, verbose_name='Опубликован'),
        ),
        migrations.AddField(
            model_name='topic',
            name='end',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата окончания'),
        ),
        migrations.AddField(
            model_name='topic',
            name='start',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата окончания'),
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='course',
            name='tutor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='task',
            name='text',
            field=models.TextField(blank=True, verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Учебная тема'), (1, 'Классная работа'), (2, 'Самостоятельная работа')], default=0, verbose_name='Тип'),
        ),
    ]
