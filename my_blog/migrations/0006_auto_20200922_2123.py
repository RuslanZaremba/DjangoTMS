# Generated by Django 3.1.1 on 2020-09-22 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0005_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
    ]