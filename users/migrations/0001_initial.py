# Generated by Django 4.2.4 on 2023-08-12 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=120)),
                ('password', models.CharField(max_length=120)),
            ],
        ),
    ]
