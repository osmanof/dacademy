# Generated by Django 5.0.3 on 2024-03-17 09:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_rename_classcoursetopic_groupcoursetopic_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='courses.topic'),
        ),
    ]
