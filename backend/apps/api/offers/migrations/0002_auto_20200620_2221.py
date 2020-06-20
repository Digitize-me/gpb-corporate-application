# Generated by Django 3.0.7 on 2020-06-20 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='tags',
        ),
        migrations.AddField(
            model_name='tagoffer',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, related_name='offers', to='offers.Offer', verbose_name='Теги'),
        ),
    ]
