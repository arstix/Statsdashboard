# Generated by Django 3.1.3 on 2020-12-10 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfoliomain', '0004_auto_20201210_2151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='tags',
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(to='Portfoliomain.Tag'),
        ),
    ]
