# Generated by Django 3.2.5 on 2021-07-11 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erAIser', '0004_rename_videofile_video_content'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='video',
            options={'verbose_name': 'video', 'verbose_name_plural': 'videos'},
        ),
        migrations.AlterField(
            model_name='video',
            name='content',
            field=models.FileField(null=True, upload_to='videos/'),
        ),
    ]