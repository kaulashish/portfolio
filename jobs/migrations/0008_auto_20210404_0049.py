# Generated by Django 3.1.7 on 2021-04-03 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0007_auto_20210404_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='phone',
            field=models.CharField(max_length=10),
        ),
    ]