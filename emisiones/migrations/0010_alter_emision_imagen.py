# Generated by Django 4.2 on 2023-09-27 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emisiones', '0009_emision_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emision',
            name='imagen',
            field=models.ImageField(null=True, upload_to='imagenesEmisiones'),
        ),
    ]
