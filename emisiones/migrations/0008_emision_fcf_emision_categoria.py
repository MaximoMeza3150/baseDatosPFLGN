# Generated by Django 4.2 on 2023-07-06 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emisiones', '0007_emision_emisionsuperada_alter_emision_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='emision',
            name='FCF',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='emision',
            name='categoria',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
