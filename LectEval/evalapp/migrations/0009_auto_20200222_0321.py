# Generated by Django 3.0.3 on 2020-02-21 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evalapp', '0008_comment_created_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='contents',
            new_name='text',
        ),
    ]
