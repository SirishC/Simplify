# Generated by Django 2.2.1 on 2019-05-09 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simplify', '0002_simpleurl_shortcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simpleurl',
            name='shortcode',
            field=models.CharField(blank=True, max_length=15, unique=True),
        ),
    ]