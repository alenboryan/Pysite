# Generated by Django 3.2.24 on 2024-06-29 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0006_auto_20240525_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studying',
            name='title',
            field=models.CharField(default=None, max_length=500),
        ),
    ]
