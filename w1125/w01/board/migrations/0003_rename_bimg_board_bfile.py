# Generated by Django 5.1.3 on 2024-11-25 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_board_bimg'),
    ]

    operations = [
        migrations.RenameField(
            model_name='board',
            old_name='bimg',
            new_name='bfile',
        ),
    ]
