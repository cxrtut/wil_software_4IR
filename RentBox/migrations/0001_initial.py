# Generated by Django 5.1.2 on 2024-11-01 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catering',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264, unique=True)),
                ('desc', models.CharField(max_length=264)),
                ('price_per_day', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.IntegerField()),
                ('replacement_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image_url', models.CharField(max_length=265)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='guest', max_length=50, unique=True)),
                ('email', models.EmailField(max_length=50, null=True, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profile_pic/CustomerProfilePic/')),
                ('address', models.CharField(max_length=40)),
                ('mobile', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Decor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264, unique=True)),
                ('desc', models.CharField(max_length=264)),
                ('price_per_day', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.IntegerField()),
                ('replacement_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image_url', models.CharField(max_length=265)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Miscellaneous',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264, unique=True)),
                ('desc', models.CharField(max_length=264)),
                ('price_per_day', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.IntegerField()),
                ('replacement_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image_url', models.CharField(max_length=265)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Seatings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264, unique=True)),
                ('desc', models.CharField(max_length=264)),
                ('price_per_day', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.IntegerField()),
                ('replacement_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image_url', models.CharField(max_length=265)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264, unique=True)),
                ('desc', models.CharField(max_length=264)),
                ('price_per_day', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.IntegerField()),
                ('replacement_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image_url', models.CharField(max_length=265)),
                ('dimensions', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]