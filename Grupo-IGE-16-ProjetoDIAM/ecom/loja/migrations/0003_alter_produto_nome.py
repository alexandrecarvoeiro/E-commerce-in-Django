# Generated by Django 5.0.6 on 2024-05-09 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0002_rename_image_produto_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='nome',
            field=models.CharField(max_length=200),
        ),
    ]
