# Generated by Django 4.2 on 2023-04-30 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty_app', '0006_leave'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='reason',
            field=models.CharField(default='approval pending', max_length=255),
        ),
    ]
