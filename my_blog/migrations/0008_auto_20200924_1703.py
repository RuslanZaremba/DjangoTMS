# Generated by Django 3.1.1 on 2020-09-24 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0007_comment_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]