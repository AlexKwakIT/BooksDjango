# Generated by Django 4.0.4 on 2022-05-01 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0025_book_in_collection_alter_book_genres'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Serie',
            new_name='Series',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='serie',
            new_name='series',
        ),
    ]
