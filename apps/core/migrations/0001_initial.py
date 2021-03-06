# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-12-08 15:19
from __future__ import unicode_literals

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
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Title')),
                ('content', models.TextField(max_length=20000, verbose_name=b'Details')),
                ('createDate', models.DateTimeField(auto_now_add=True, verbose_name=b'CreatedDate')),
                ('startDate', models.DateTimeField(blank=True, null=True, verbose_name=b'StartDate')),
                ('endDate', models.DateTimeField(blank=True, null=True, verbose_name=b'EndDate')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name=b'timeUpdated')),
                ('firstPicture', models.ImageField(blank=True, upload_to=b'action/images')),
            ],
            options={
                'verbose_name': 'Action',
                'verbose_name_plural': 'Actions',
            },
        ),
        migrations.CreateModel(
            name='ActionPicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, upload_to=b'action/images')),
                ('actionid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Action')),
            ],
            options={
                'verbose_name': 'ActionPicture',
                'verbose_name_plural': 'ActionPictures',
            },
        ),
        migrations.CreateModel(
            name='ActionRefLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.TextField(max_length=1000)),
                ('actionid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Action')),
            ],
            options={
                'verbose_name': 'ActionRefLink',
                'verbose_name_plural': 'ActionRefLinks',
            },
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_type', models.CharField(choices=[(b'F', b'Favorite'), (b'L', b'Like'), (b'U', b'Up Vote'), (b'D', b'Down Vote')], max_length=1)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('feed', models.IntegerField(blank=True, null=True)),
                ('question', models.IntegerField(blank=True, null=True)),
                ('answer', models.IntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Activity',
                'verbose_name_plural': 'Activities',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=2000)),
                ('createDate', models.DateTimeField(auto_now_add=True, verbose_name=b'CreatedDate')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name=b'timeUdated')),
                ('active', models.BooleanField()),
                ('childcomment', models.ManyToManyField(related_name='_comment_childcomment_+', to='core.Comment')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=2000)),
                ('isaccept', models.BooleanField()),
                ('createDate', models.DateTimeField(auto_now_add=True, verbose_name=b'CreatedD')),
            ],
            options={
                'verbose_name': 'Invitation',
                'verbose_name_plural': 'Invitations',
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdDate', models.DateTimeField(auto_now_add=True)),
                ('notificationtype', models.CharField(choices=[(b'L', b'Liked'), (b'C', b'Commented'), (b'A', b'accepted'), (b'D', b'deadlined'), (b'F', b'ClosedAction'), (b'R', b'ReplyComment')], max_length=1)),
                ('isread', models.BooleanField(default=False)),
                ('action', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Action')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Comment')),
                ('inviation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Invitation')),
            ],
            options={
                'ordering': ('-createdDate',),
                'verbose_name': 'Notification',
                'verbose_name_plural': 'Notifications',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('gender', models.CharField(choices=[(b'M', b'Male'), (b'F', b'Female')], max_length=1)),
                ('occupation', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('createdDate', models.DateTimeField(auto_now_add=True)),
                ('last_active', models.DateTimeField(auto_now_add=True)),
                ('birthday', models.DateTimeField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'UserProfile',
                'verbose_name_plural': 'UserProfiles',
            },
        ),
        migrations.AddField(
            model_name='invitation',
            name='fromuser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='core.UserProfile'),
        ),
        migrations.AddField(
            model_name='invitation',
            name='touser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='core.UserProfile'),
        ),
        migrations.AddField(
            model_name='comment',
            name='commentby',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.UserProfile'),
        ),
        migrations.AddField(
            model_name='comment',
            name='commentin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Action'),
        ),
        migrations.AddField(
            model_name='action',
            name='actionPictures',
            field=models.ManyToManyField(blank=True, to='core.ActionPicture', verbose_name=b'list pictures'),
        ),
        migrations.AddField(
            model_name='action',
            name='likeby',
            field=models.ManyToManyField(blank=True, to='core.UserProfile', verbose_name=b'likers'),
        ),
        migrations.AddField(
            model_name='action',
            name='listComment',
            field=models.ManyToManyField(blank=True, to='core.Comment', verbose_name=b'listComment'),
        ),
        migrations.AddField(
            model_name='action',
            name='listRefLink',
            field=models.ManyToManyField(blank=True, to='core.ActionRefLink', verbose_name=b'ListRefLink'),
        ),
    ]
