# Generated by Django 3.2.2 on 2021-12-08 04:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('year', models.CharField(max_length=50)),
                ('genres', models.CharField(max_length=50)),
                ('summary', models.CharField(max_length=50)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='MovieReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=50)),
                ('rating', models.CharField(max_length=50)),
                ('created_at', models.CharField(max_length=50)),
                ('summary', models.CharField(max_length=50)),
                ('is_deleted', models.BooleanField(default=False)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='movieapp.movie')),
            ],
        ),
        migrations.CreateModel(
            name='MovieReviewVote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('review_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='movieapp.moviereview')),
            ],
        ),
    ]
