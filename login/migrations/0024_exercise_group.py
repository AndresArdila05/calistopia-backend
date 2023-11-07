# Generated by Django 4.2.5 on 2023-11-06 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0023_alter_exercise_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='group',
            field=models.CharField(blank=True, choices=[('L', 'LEGS'), ('AR', 'ARMS'), ('AB', 'ABDOMINALS'), ('C', 'CHEST'), ('B', 'BACK'), ('S', 'SHOULDERS')]),
        ),
    ]