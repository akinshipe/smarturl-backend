# Generated by Django 4.0.2 on 2022-02-27 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_url_last_visit_url_last_visit_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='last_visit_time',
            field=models.DateField(null=True),
        ),
    ]
