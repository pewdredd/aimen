# Generated by Django 5.0 on 2024-07-17 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aibots', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aibotorder',
            name='title',
            field=models.CharField(default='Test', max_length=255, verbose_name='Название'),
            preserve_default=False,
        ),
    ]
