# Generated by Django 4.2 on 2023-07-01 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emisiones', '0002_alter_emisiones_area_alter_emisiones_ciclado_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='emisiones',
            name='operador',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]