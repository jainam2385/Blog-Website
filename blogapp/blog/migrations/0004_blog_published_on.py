# Generated by Django 3.2 on 2021-04-09 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='published_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]