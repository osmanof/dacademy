# Generated by Django 5.0.2 on 2024-03-04 07:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0006_group_groupcourses_group_courses_groupstudent_and_more'),
        ('courses', '0003_rename_tutor_course_author'),
        ('users', '0004_student_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='task',
            name='format_in_text',
            field=models.TextField(blank=True, null=True, verbose_name='Формат входных данных'),
        ),
        migrations.AddField(
            model_name='task',
            name='format_out_text',
            field=models.TextField(blank=True, null=True, verbose_name='Формат выходных данных'),
        ),
        migrations.AddField(
            model_name='topic',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='course',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.teacher'),
        ),
        migrations.CreateModel(
            name='Attempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField(verbose_name='Код решения')),
                ('status', models.PositiveSmallIntegerField(verbose_name='Статус попытки')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.student')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.task')),
            ],
            options={
                'verbose_name': 'Попытка',
                'verbose_name_plural': 'Попытки',
            },
        ),
        migrations.CreateModel(
            name='ClassCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Удален')),
                ('class_field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.group')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
            ],
            options={
                'verbose_name': 'Курс класса',
                'verbose_name_plural': 'Курсы класса',
            },
        ),
        migrations.CreateModel(
            name='ClassCourseTopic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opened', models.BooleanField(default=False, verbose_name='Открыт')),
                ('deadline_at', models.DateTimeField(verbose_name='Дедлайн до')),
                ('class_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.classcourse')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.topic')),
            ],
            options={
                'verbose_name': 'Тема курса класса',
                'verbose_name_plural': 'Темы курса класса',
            },
        ),
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stdin', models.CharField(max_length=256, verbose_name='Входные данные')),
                ('stdout', models.CharField(max_length=256, verbose_name='Выходные данные')),
                ('timelimit', models.IntegerField(verbose_name='Ограничение по времени')),
                ('ram_limit', models.IntegerField(verbose_name='Ограничение по памяти')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.task')),
            ],
            options={
                'verbose_name': 'Тест-кейс',
                'verbose_name_plural': 'Тест-кейсы',
            },
        ),
        migrations.DeleteModel(
            name='Solution',
        ),
    ]
