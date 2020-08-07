# Generated by Django 3.0.8 on 2020-08-07 09:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


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
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('user_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chatto', to=settings.AUTH_USER_MODEL)),
                ('user_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chatfrom', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
