# Generated by Django 3.0.8 on 2020-07-17 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IpAddr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cidr', models.CharField(max_length=20, unique=True)),
                ('status', models.CharField(choices=[('available', 'Available'), ('acquired', 'Acquired')], default='available', max_length=100)),
            ],
        ),
    ]
