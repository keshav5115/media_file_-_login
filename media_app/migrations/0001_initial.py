# Generated by Django 4.1.3 on 2022-11-23 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('phone', models.PositiveBigIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('sal', models.IntegerField()),
                ('gender', models.CharField(choices=[['male', 'male'], ['female', 'female']], max_length=20)),
                ('date', models.DateField(auto_now=True)),
                ('photo', models.ImageField(upload_to='img')),
                ('resume', models.FileField(upload_to='resume')),
            ],
        ),
    ]
