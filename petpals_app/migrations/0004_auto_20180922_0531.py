# Generated by Django 2.0.5 on 2018-09-22 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petpals_app', '0003_auto_20180922_0502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='profile_picture',
            field=models.ImageField(blank=True, upload_to='petpals_app/media'),
        ),
    ]
