# Generated by Django 4.1.5 on 2023-02-10 19:29

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=255, verbose_name='Category Name')),
                ('category_status', models.IntegerField(default=1, max_length=255, verbose_name='Category Status')),
                ('created_at', models.DateField(default=datetime.date.today)),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=255, verbose_name='Blog Title')),
                ('blog_description', models.TextField(verbose_name='Blog Description')),
                ('blog_featured_image', models.ImageField(max_length=255, upload_to='images/')),
                ('status', models.IntegerField(default=1, max_length=10)),
                ('blog_posted_date', models.DateField(default=datetime.date.today)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.category')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'blogs',
            },
        ),
    ]
