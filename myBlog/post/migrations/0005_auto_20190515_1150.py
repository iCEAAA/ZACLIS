# Generated by Django 2.2 on 2019-05-15 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20190424_1746'),
    ]

    operations = [
        migrations.CreateModel(
            name='tag',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='name')),
                ('description', models.CharField(max_length=100, verbose_name='description')),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='id',
        ),
        migrations.AddField(
            model_name='post',
            name='modify_time',
            field=models.DateField(default='2019-5-15', verbose_name='modify_time'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='title'),
        ),
    ]
