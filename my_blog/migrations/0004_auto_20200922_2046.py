# Generated by Django 3.1.1 on 2020-09-22 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0003_post_draft'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
    ]