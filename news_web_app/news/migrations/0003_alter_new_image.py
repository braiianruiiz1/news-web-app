# Generated by Django 4.0.6 on 2022-07-12 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_new_options_new_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='news', verbose_name='Imagen'),
        ),
    ]
