# Generated by Django 4.0.3 on 2022-04-01 10:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('books', '0006_book_remarks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(blank=True, max_length=40, null=True, unique=True, verbose_name='ISBN'),
        ),
    ]
