# Generated by Django 4.1.1 on 2022-09-11 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutme', '0003_pieces'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pieces',
            name='difficulty',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='pieces',
            name='status',
            field=models.PositiveIntegerField(),
        ),
    ]
