# Generated by Django 4.1.7 on 2023-03-01 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0003_alter_ads_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='ads'),
        ),
    ]
