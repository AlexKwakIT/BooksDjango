# Generated by Django 4.0.4 on 2022-06-06 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0040_alter_video_options_rename_kind_video_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='screen_width',
            field=models.IntegerField(default=0),
        ),
    ]