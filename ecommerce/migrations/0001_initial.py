# Generated by Django 3.0.2 on 2020-01-20 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cus_user', models.CharField(max_length=200)),
                ('user', models.CharField(max_length=200)),
                ('password', models.TextField()),
            ],
        ),
    ]
