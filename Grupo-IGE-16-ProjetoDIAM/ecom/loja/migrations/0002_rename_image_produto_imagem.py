# Generated by Django 5.0.6 on 2024-05-09 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produto',
            old_name='image',
            new_name='imagem',
        ),
    ]
