# Generated by Django 4.0.2 on 2022-02-27 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_url_visits'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='last_visit',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='url',
            name='created_time',
            field=models.DateField(auto_now=True),
        ),
    ]
