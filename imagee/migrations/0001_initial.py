# Generated by Django 4.1.2 on 2022-11-01 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='image')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]