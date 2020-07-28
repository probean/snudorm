# Generated by Django 3.0.5 on 2020-07-28 02:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('content', models.TextField()),
                ('photo', models.ImageField(blank=True, upload_to='feed_photos')),
                ('noname', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('views', models.IntegerField(blank=True, default=0)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created_at',),
            },
        ),
        migrations.CreateModel(
            name='FeedComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('noname', models.BooleanField(default=False)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('feed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedpage.Feed')),
                ('like_users', models.ManyToManyField(blank=True, related_name='like_comments', through='feedpage.CommentLike', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Recomment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('noname', models.BooleanField(default=False)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedpage.FeedComment')),
            ],
        ),
        migrations.CreateModel(
            name='FreeBoard',
            fields=[
                ('feed_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='feedpage.Feed')),
            ],
            bases=('feedpage.feed',),
        ),
        migrations.CreateModel(
            name='Life',
            fields=[
                ('feed_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='feedpage.Feed')),
                ('product', models.CharField(max_length=256)),
                ('contact', models.CharField(max_length=256)),
                ('status', models.CharField(max_length=256)),
            ],
            options={
                'ordering': ('created_at',),
            },
            bases=('feedpage.feed',),
        ),
        migrations.CreateModel(
            name='Minwon',
            fields=[
                ('feed_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='feedpage.Feed')),
                ('dormitory', models.CharField(max_length=20)),
                ('building', models.CharField(max_length=20)),
            ],
            bases=('feedpage.feed',),
        ),
        migrations.CreateModel(
            name='RecommentLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('recomment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedpage.Recomment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FeedLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('feed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedlike', to='feedpage.Feed')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='feed',
            name='like_users',
            field=models.ManyToManyField(blank=True, related_name='like_feeds', through='feedpage.FeedLike', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='commentlike',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedpage.FeedComment'),
        ),
        migrations.AddField(
            model_name='commentlike',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='CoBuy',
            fields=[
                ('life_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='feedpage.Life')),
                ('price', models.IntegerField(blank=True)),
                ('duedate', models.DateTimeField(blank=True)),
                ('url', models.CharField(max_length=256, null=True)),
            ],
            bases=('feedpage.life',),
        ),
        migrations.CreateModel(
            name='Keep',
            fields=[
                ('life_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='feedpage.Life')),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('reward', models.CharField(max_length=256)),
            ],
            bases=('feedpage.life',),
        ),
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('life_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='feedpage.Life')),
                ('deposit', models.CharField(max_length=256)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
            ],
            bases=('feedpage.life',),
        ),
        migrations.CreateModel(
            name='Resell',
            fields=[
                ('life_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='feedpage.Life')),
                ('price', models.IntegerField(blank=True)),
                ('role', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('seller', '판매자'), ('buyer', '구매자')], max_length=12, null=True)),
            ],
            bases=('feedpage.life',),
        ),
    ]
