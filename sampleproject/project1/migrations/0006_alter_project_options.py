# Generated by Django 3.2.6 on 2021-08-18 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project1', '0005_auto_20210818_0525'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-vote_ratio', '-vote_total', 'title']},
        ),
    ]
