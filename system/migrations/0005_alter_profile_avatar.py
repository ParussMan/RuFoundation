# Generated by Django 4.0.4 on 2022-06-09 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0004_alter_profile_avatar_alter_profile_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='/static/images/default_avatar.png', upload_to='-/users', verbose_name='Аватар'),
        ),
    ]
