# Generated by Django 2.1.7 on 2019-04-24 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20190424_1013'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='default',
            new_name='content',
        ),
    ]