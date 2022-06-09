# Generated by Django 4.0.4 on 2022-06-09 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0019_alter_vote_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Имя')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'permissions': [('can_add_article_in_category', 'Может добавлять новые статьи в категорию'), ('can_change_article_in_category', 'Может изменять статьи в категории'), ('can_delete_article_in_category', 'Может удалять статьи в категории'), ('can_vote_article_in_category', 'Может голосовать за статьи в категории')],
            },
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'permissions': [('can_vote_article', 'Может голосовать за статью')], 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.AddIndex(
            model_name='category',
            index=models.Index(fields=['name'], name='web_categor_name_e51bae_idx'),
        ),
        migrations.AddConstraint(
            model_name='category',
            constraint=models.UniqueConstraint(fields=('name',), name='web_category_unique'),
        ),
    ]