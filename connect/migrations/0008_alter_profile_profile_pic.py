# Generated by Django 4.0.5 on 2022-06-07 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0007_alter_profile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='DEFAULT VALUE', upload_to='profile-images/'),
        ),
    ]
