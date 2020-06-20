# Generated by Django 3.0.7 on 2020-06-20 14:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reference', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.BooleanField(default=False, verbose_name='Публикация')),
                ('date_created', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('idea_short', models.CharField(max_length=255, verbose_name='Краткое мероприятия')),
                ('idea', models.TextField(verbose_name='Подробное описание')),
                ('date_of_the_event', models.DateField(verbose_name='Дата проведения')),
                ('img', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='reference.Category', verbose_name='Категория')),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Создатель')),
                ('tags', models.ManyToManyField(to='reference.Tag', verbose_name='Теги')),
            ],
            options={
                'verbose_name': 'Мероприятие',
                'verbose_name_plural': 'Мероприятия',
            },
        ),
    ]