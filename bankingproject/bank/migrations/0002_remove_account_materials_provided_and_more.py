# Generated by Django 4.2.4 on 2023-08-29 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='materials_provided',
        ),
        migrations.AddField(
            model_name='account',
            name='materials_provided',
            field=models.BooleanField(default=False),
        ),
    ]
