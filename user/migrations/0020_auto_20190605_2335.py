# Generated by Django 2.2.1 on 2019-06-05 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0019_auto_20190604_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pic',
            field=models.FileField(max_length=64, upload_to='', verbose_name='封面图片'),
        ),
    ]
