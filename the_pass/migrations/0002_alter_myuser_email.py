# Generated by Django 5.0.3 on 2024-04-10 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('the_pass', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='email',
            field=models.EmailField(max_length=200),
        ),
    ]
