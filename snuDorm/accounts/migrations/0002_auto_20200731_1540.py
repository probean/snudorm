# Generated by Django 3.0.8 on 2020-07-31 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='building_category',
            field=models.CharField(choices=[('bachelor', '학부생활관'), ('master', '대학원생활관'), ('family', '가족생활관'), ('BK', 'BK생활관')], max_length=20, verbose_name='생활관'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='building_dong',
            field=models.CharField(choices=[('902', '902동'), ('903', '903동'), ('901', '901동'), ('905', '905동'), ('906', '906동'), ('900', '900동'), ('904', '904동')], max_length=20, verbose_name='동'),
        ),
    ]