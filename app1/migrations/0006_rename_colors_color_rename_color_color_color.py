# Generated by Django 5.0.4 on 2024-04-19 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_colors_product_color'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Colors',
            new_name='Color',
        ),
        migrations.RenameField(
            model_name='color',
            old_name='Color',
            new_name='color',
        ),
    ]
