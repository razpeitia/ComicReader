# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('createTime', models.DateTimeField(auto_now_add=True)),
                ('updateTime', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True)),
                ('cover', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('slug', models.SlugField(unique=True)),
                ('publisher', models.CharField(max_length=100)),
                ('release_date', models.DateField()),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('createTime', models.DateTimeField(auto_now_add=True)),
                ('updateTime', models.DateTimeField(auto_now=True)),
                ('text', models.TextField()),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CommentVote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('createTime', models.DateTimeField(auto_now_add=True)),
                ('updateTime', models.DateTimeField(auto_now=True)),
                ('comment', models.ForeignKey(to='reader.Comment')),
                ('voter', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('createTime', models.DateTimeField(auto_now_add=True)),
                ('updateTime', models.DateTimeField(auto_now=True)),
                ('number', models.IntegerField()),
                ('title', models.CharField(max_length=200)),
                ('comic', models.ForeignKey(to='reader.Comic')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('createTime', models.DateTimeField(auto_now_add=True)),
                ('updateTime', models.DateTimeField(auto_now=True)),
                ('page_number', models.PositiveIntegerField()),
                ('image', models.ImageField(upload_to=b'')),
                ('issue', models.ForeignKey(to='reader.Issue')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='page',
            unique_together=set([('issue', 'page_number')]),
        ),
        migrations.AlterUniqueTogether(
            name='issue',
            unique_together=set([('comic', 'number')]),
        ),
        migrations.AlterUniqueTogether(
            name='commentvote',
            unique_together=set([('voter', 'comment')]),
        ),
        migrations.AddField(
            model_name='comment',
            name='page',
            field=models.ForeignKey(to='reader.Issue'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
