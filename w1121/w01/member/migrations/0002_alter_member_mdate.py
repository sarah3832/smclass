# Generated by Django 5.1.3 on 2024-11-21 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='mdate',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
