# Generated by Django 4.0.6 on 2022-08-12 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_alter_article_options_alter_category_options_and_more'),
    ]

    operations = [
        migrations.RunSQL('UPDATE web_article a SET author_id=v.user_id FROM web_articlelogentry v WHERE v.article_id=a.id AND v.rev_number=0')
    ]
