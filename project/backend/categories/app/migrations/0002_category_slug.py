# Generated by Django 4.0.3 on 2022-03-13 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='none', max_length=256),
            preserve_default=False,
        ),
    ]
