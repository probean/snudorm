# Generated by Django 3.0.8 on 2020-08-05 21:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='이름')),
                ('nickname', models.CharField(max_length=15, verbose_name='닉네임')),
                ('building_category', models.CharField(max_length=20, verbose_name='생활관')),
                ('building_dong', models.CharField(max_length=20, verbose_name='동')),
                ('email', models.CharField(max_length=20, verbose_name='이메일')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
