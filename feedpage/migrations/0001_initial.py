# Generated by Django 3.0.8 on 2020-08-18 19:42

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
                ('noname', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('views', models.IntegerField(blank=True, default=0)),
                ('notice', models.BooleanField(default=False)),
                ('board', models.CharField(max_length=256)),
                ('category', models.CharField(max_length=256)),
                ('board_info1', models.CharField(max_length=20)),
                ('board_info2', models.CharField(max_length=20)),
                ('status', multiselectfield.db.fields.MultiSelectField(choices=[('ongoing', '진행중'), ('onsale', '판매중'), ('complete', '완료')], default='ongoing', max_length=23)),
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
        migrations.AddField(
            model_name='recomment',
            name='like_users',
            field=models.ManyToManyField(blank=True, related_name='like_recomments', through='feedpage.RecommentLike', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_info1', models.CharField(max_length=20)),
                ('type_info2', models.CharField(max_length=20, null=True)),
                ('checked', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('noname', models.BooleanField(default=False)),
                ('feed', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notification', to='feedpage.Feed')),
                ('user_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mylog', to=settings.AUTH_USER_MODEL)),
                ('user_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mynotice', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='feed_photos')),
                ('feed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedpage.Feed')),
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
                ('price', models.CharField(max_length=256)),
                ('url', models.CharField(max_length=256, null=True)),
                ('duedate', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            bases=('feedpage.life',),
        ),
        migrations.CreateModel(
            name='Keep',
            fields=[
                ('life_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='feedpage.Life')),
                ('purpose', multiselectfield.db.fields.MultiSelectField(choices=[('lender', '보관할래요'), ('user', '보관해줄게요')], default='lender', max_length=11)),
                ('reward', models.CharField(max_length=256)),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            bases=('feedpage.life',),
        ),
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('life_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='feedpage.Life')),
                ('purpose', multiselectfield.db.fields.MultiSelectField(choices=[('lender', '빌려줄게요'), ('user', '빌려주세요')], default='lender', max_length=11)),
                ('deposit', models.CharField(max_length=256)),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            bases=('feedpage.life',),
        ),
        migrations.CreateModel(
            name='Resell',
            fields=[
                ('life_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='feedpage.Life')),
                ('purpose', multiselectfield.db.fields.MultiSelectField(choices=[('seller', '판매'), ('buyer', '구매')], default='seller', max_length=12)),
                ('price', models.CharField(max_length=256)),
            ],
            bases=('feedpage.life',),
        ),
    ]
