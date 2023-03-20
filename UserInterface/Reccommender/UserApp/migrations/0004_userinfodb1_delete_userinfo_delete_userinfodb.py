# Generated by Django 4.1 on 2023-03-12 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0003_alter_userinfodb_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfoDB1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('college', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('key_enc', models.CharField(max_length=150)),
            ],
        ),
        migrations.DeleteModel(
            name='UserInfo',
        ),
        migrations.DeleteModel(
            name='UserInfoDB',
        ),
    ]
