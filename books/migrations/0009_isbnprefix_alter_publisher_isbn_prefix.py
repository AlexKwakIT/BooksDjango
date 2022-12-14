# Generated by Django 4.0.3 on 2022-04-02 15:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('books', '0008_publisher_isbn_prefix'),
    ]

    operations = [
        migrations.CreateModel(
            name='IsbnPrefix',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prefix', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='publisher',
            name='isbn_prefix',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    to='books.isbnprefix'),
        ),
    ]
