# Generated by Django 2.1.3 on 2019-01-09 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0004_auto_20190109_1009'),
    ]

    operations = [
        migrations.AddField(
            model_name='dbserver',
            name='region',
            field=models.CharField(blank=True, max_length=16, null=True, verbose_name='区域'),
        ),
    ]