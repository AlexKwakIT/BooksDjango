# Generated by Django 4.0.3 on 2022-04-16 13:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('books', '0012_remove_publisher_display_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
