# Generated by Django 3.1.7 on 2021-04-03 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_accomplishments_detail_education_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
