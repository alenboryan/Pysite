# Generated by Django 3.2.24 on 2024-07-01 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0008_rename_pysintax_pysyntax'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pyintro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=5000)),
            ],
        ),
    ]
