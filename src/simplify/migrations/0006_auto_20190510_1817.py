# Generated by Django 2.2.1 on 2019-05-10 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simplify', '0005_auto_20190510_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simpleurl',
            name='shortcode',
            field=models.CharField(blank=True, default='abc', max_length=15, unique=True),
        ),
    ]
