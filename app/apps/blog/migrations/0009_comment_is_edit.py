# Generated by Django 2.2.4 on 2019-09-01 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20190901_1952'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='is_edit',
            field=models.BooleanField(default=False),
        ),
    ]
