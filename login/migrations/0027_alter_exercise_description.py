# Generated by Django 4.2.5 on 2023-11-06 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0026_alter_exercise_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='description',
            field=models.TextField(unique=True),
        ),
    ]