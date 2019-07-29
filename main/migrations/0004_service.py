# Generated by Django 2.2.2 on 2019-07-08 19:24

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20190708_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('intro', models.TextField(null=True)),
                ('bg_color', colorfield.fields.ColorField(default='#ffffff', max_length=18)),
            ],
        ),
    ]