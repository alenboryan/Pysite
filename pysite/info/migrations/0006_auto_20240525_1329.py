# Generated by Django 3.2.24 on 2024-05-25 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0005_studying'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlaskInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=5000)),
            ],
        ),
        migrations.AddField(
            model_name='studying',
            name='content',
            field=models.CharField(default='', max_length=5000),
        ),
        migrations.AddField(
            model_name='studying',
            name='title',
            field=models.CharField(default='', max_length=500),
        ),
    ]
