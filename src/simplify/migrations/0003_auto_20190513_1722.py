# Generated by Django 2.2.1 on 2019-05-13 17:22

from django.db import migrations, models
import simplify.validators


class Migration(migrations.Migration):

    dependencies = [
        ('simplify', '0002_simplifyurl_shortcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simplifyurl',
            name='url',
            field=models.CharField(max_length=220, validators=[simplify.validators.validate_url]),
        ),
    ]
