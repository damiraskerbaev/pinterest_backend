# Generated by Django 4.2.8 on 2024-02-09 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Post of the title')),
                ('description', models.TextField(blank=True, verbose_name='Description of the post')),
                ('created', models.DateField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='post-images/', verbose_name='Post of the image')),
                ('watch_count', models.PositiveBigIntegerField(default=0, verbose_name='Views of the post')),
                ('like_count', models.PositiveBigIntegerField(default=0, verbose_name='Likes of the post')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='category.category')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]
