# Generated by Django 5.0.8 on 2024-08-06 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='myimage')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
