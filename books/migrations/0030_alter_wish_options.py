# Generated by Django 4.0.4 on 2022-05-01 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0029_wish'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wish',
            options={'ordering': ('author', 'title', 'remarks')},
        ),
    ]
