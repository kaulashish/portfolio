# Generated by Django 3.1.7 on 2021-04-03 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_auto_20210403_2217'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
