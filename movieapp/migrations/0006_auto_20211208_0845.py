# Generated by Django 3.2.2 on 2021-12-08 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0005_alter_moviereview_summary'),
    ]

    operations = [
        migrations.RenameField(
            model_name='moviereviewvote',
            old_name='review_id',
            new_name='review',
        ),
        migrations.RemoveField(
            model_name='moviereview',
            name='summary',
        ),
    ]
