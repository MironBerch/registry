# Generated by Django 4.1.4 on 2023-02-10 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_studentsbase'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='is_learns',
            field=models.BooleanField(default=True),
        ),
    ]
