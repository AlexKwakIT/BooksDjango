# Generated by Django 4.0.3 on 2022-04-02 20:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('books', '0009_isbnprefix_alter_publisher_isbn_prefix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING,
                                    related_name='books', to='books.publisher'),
        ),
        migrations.AlterField(
            model_name='book',
            name='serie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING,
                                    related_name='books', to='books.serie'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='isbn_prefix',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING,
                                    to='books.isbnprefix'),
        ),
    ]
