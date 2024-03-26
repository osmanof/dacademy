# Generated by Django 5.0.2 on 2024-03-02 06:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150, verbose_name='Заголовок')),
                ('text', models.CharField(blank=True, max_length=150, verbose_name='Текст')),
                ('autocheck', models.BooleanField(default=False, verbose_name='autocheck')),
                ('stdin', models.TextField(verbose_name='stdin')),
                ('stdout', models.TextField(verbose_name='stdout')),
                ('samples', models.TextField(verbose_name='samples')),
                ('tests', models.TextField(verbose_name='tests')),
            ],
            options={
                'verbose_name': 'Задание',
                'verbose_name_plural': 'Задания',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150, verbose_name='Заголовок')),
                ('public', models.BooleanField(default=False, verbose_name='Опубликован')),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField(verbose_name='code')),
                ('status', models.PositiveSmallIntegerField(verbose_name='status')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.task')),
            ],
            options={
                'verbose_name': 'Решение',
                'verbose_name_plural': 'Решения',
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150, verbose_name='Заголовок')),
                ('deadline', models.DateTimeField()),
                ('type', models.PositiveSmallIntegerField(verbose_name='Тип')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
            ],
            options={
                'verbose_name': 'Тема',
                'verbose_name_plural': 'Темы',
            },
        ),
        migrations.AddField(
            model_name='task',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.topic'),
        ),
    ]
