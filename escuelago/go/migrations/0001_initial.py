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
            name='Match',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('black_rank', models.CharField(default=b'20k', max_length=3, choices=[(b'9p', b'9 dan pro'), (b'8p', b'8 dan pro'), (b'7p', b'7 dan pro'), (b'6p', b'6 dan pro'), (b'5p', b'5 dan pro'), (b'4p', b'4 dan pro'), (b'3p', b'3 dan pro'), (b'2p', b'2 dan pro'), (b'1p', b'1 dan pro'), (b'9d', b'9 dan'), (b'8d', b'8 dan'), (b'7d', b'7 dan'), (b'6d', b'6 dan'), (b'5d', b'5 dan'), (b'4d', b'4 dan'), (b'3d', b'3 dan'), (b'2d', b'2 dan'), (b'1d', b'1 dan'), (b'1k', b'1 kyu'), (b'2k', b'2 kyu'), (b'3k', b'3 kyu'), (b'4k', b'4 kyu'), (b'5k', b'5 kyu'), (b'6k', b'6 kyu'), (b'7k', b'7 kyu'), (b'8k', b'8 kyu'), (b'9k', b'9 kyu'), (b'10k', b'10 kyu'), (b'11k', b'11 kyu'), (b'12k', b'12 kyu'), (b'13k', b'13 kyu'), (b'14k', b'14 kyu'), (b'15k', b'15 kyu'), (b'16k', b'16 kyu'), (b'17k', b'17 kyu'), (b'18k', b'18 kyu'), (b'19k', b'19 kyu'), (b'20k', b'20 kyu')])),
                ('white_rank', models.CharField(default=b'20k', max_length=3, choices=[(b'9p', b'9 dan pro'), (b'8p', b'8 dan pro'), (b'7p', b'7 dan pro'), (b'6p', b'6 dan pro'), (b'5p', b'5 dan pro'), (b'4p', b'4 dan pro'), (b'3p', b'3 dan pro'), (b'2p', b'2 dan pro'), (b'1p', b'1 dan pro'), (b'9d', b'9 dan'), (b'8d', b'8 dan'), (b'7d', b'7 dan'), (b'6d', b'6 dan'), (b'5d', b'5 dan'), (b'4d', b'4 dan'), (b'3d', b'3 dan'), (b'2d', b'2 dan'), (b'1d', b'1 dan'), (b'1k', b'1 kyu'), (b'2k', b'2 kyu'), (b'3k', b'3 kyu'), (b'4k', b'4 kyu'), (b'5k', b'5 kyu'), (b'6k', b'6 kyu'), (b'7k', b'7 kyu'), (b'8k', b'8 kyu'), (b'9k', b'9 kyu'), (b'10k', b'10 kyu'), (b'11k', b'11 kyu'), (b'12k', b'12 kyu'), (b'13k', b'13 kyu'), (b'14k', b'14 kyu'), (b'15k', b'15 kyu'), (b'16k', b'16 kyu'), (b'17k', b'17 kyu'), (b'18k', b'18 kyu'), (b'19k', b'19 kyu'), (b'20k', b'20 kyu')])),
                ('handicap', models.IntegerField(null=True, blank=True)),
                ('reviewer_rank', models.CharField(default=b'20k', max_length=3, choices=[(b'9p', b'9 dan pro'), (b'8p', b'8 dan pro'), (b'7p', b'7 dan pro'), (b'6p', b'6 dan pro'), (b'5p', b'5 dan pro'), (b'4p', b'4 dan pro'), (b'3p', b'3 dan pro'), (b'2p', b'2 dan pro'), (b'1p', b'1 dan pro'), (b'9d', b'9 dan'), (b'8d', b'8 dan'), (b'7d', b'7 dan'), (b'6d', b'6 dan'), (b'5d', b'5 dan'), (b'4d', b'4 dan'), (b'3d', b'3 dan'), (b'2d', b'2 dan'), (b'1d', b'1 dan'), (b'1k', b'1 kyu'), (b'2k', b'2 kyu'), (b'3k', b'3 kyu'), (b'4k', b'4 kyu'), (b'5k', b'5 kyu'), (b'6k', b'6 kyu'), (b'7k', b'7 kyu'), (b'8k', b'8 kyu'), (b'9k', b'9 kyu'), (b'10k', b'10 kyu'), (b'11k', b'11 kyu'), (b'12k', b'12 kyu'), (b'13k', b'13 kyu'), (b'14k', b'14 kyu'), (b'15k', b'15 kyu'), (b'16k', b'16 kyu'), (b'17k', b'17 kyu'), (b'18k', b'18 kyu'), (b'19k', b'19 kyu'), (b'20k', b'20 kyu')])),
                ('sgf', models.CharField(max_length=2048)),
                ('status', models.CharField(default=b'20k', max_length=3, choices=[(b'9p', b'9 dan pro'), (b'8p', b'8 dan pro'), (b'7p', b'7 dan pro'), (b'6p', b'6 dan pro'), (b'5p', b'5 dan pro'), (b'4p', b'4 dan pro'), (b'3p', b'3 dan pro'), (b'2p', b'2 dan pro'), (b'1p', b'1 dan pro'), (b'9d', b'9 dan'), (b'8d', b'8 dan'), (b'7d', b'7 dan'), (b'6d', b'6 dan'), (b'5d', b'5 dan'), (b'4d', b'4 dan'), (b'3d', b'3 dan'), (b'2d', b'2 dan'), (b'1d', b'1 dan'), (b'1k', b'1 kyu'), (b'2k', b'2 kyu'), (b'3k', b'3 kyu'), (b'4k', b'4 kyu'), (b'5k', b'5 kyu'), (b'6k', b'6 kyu'), (b'7k', b'7 kyu'), (b'8k', b'8 kyu'), (b'9k', b'9 kyu'), (b'10k', b'10 kyu'), (b'11k', b'11 kyu'), (b'12k', b'12 kyu'), (b'13k', b'13 kyu'), (b'14k', b'14 kyu'), (b'15k', b'15 kyu'), (b'16k', b'16 kyu'), (b'17k', b'17 kyu'), (b'18k', b'18 kyu'), (b'19k', b'19 kyu'), (b'20k', b'20 kyu')])),
                ('upload_day', models.DateField(help_text=b"Format: 'DD/MM/YYYY'", auto_now=True)),
                ('comments', models.CharField(default=b'20k', max_length=3, choices=[(b'9p', b'9 dan pro'), (b'8p', b'8 dan pro'), (b'7p', b'7 dan pro'), (b'6p', b'6 dan pro'), (b'5p', b'5 dan pro'), (b'4p', b'4 dan pro'), (b'3p', b'3 dan pro'), (b'2p', b'2 dan pro'), (b'1p', b'1 dan pro'), (b'9d', b'9 dan'), (b'8d', b'8 dan'), (b'7d', b'7 dan'), (b'6d', b'6 dan'), (b'5d', b'5 dan'), (b'4d', b'4 dan'), (b'3d', b'3 dan'), (b'2d', b'2 dan'), (b'1d', b'1 dan'), (b'1k', b'1 kyu'), (b'2k', b'2 kyu'), (b'3k', b'3 kyu'), (b'4k', b'4 kyu'), (b'5k', b'5 kyu'), (b'6k', b'6 kyu'), (b'7k', b'7 kyu'), (b'8k', b'8 kyu'), (b'9k', b'9 kyu'), (b'10k', b'10 kyu'), (b'11k', b'11 kyu'), (b'12k', b'12 kyu'), (b'13k', b'13 kyu'), (b'14k', b'14 kyu'), (b'15k', b'15 kyu'), (b'16k', b'16 kyu'), (b'17k', b'17 kyu'), (b'18k', b'18 kyu'), (b'19k', b'19 kyu'), (b'20k', b'20 kyu')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('current_rank', models.CharField(default=b'20k', max_length=3, choices=[(b'9p', b'9 dan pro'), (b'8p', b'8 dan pro'), (b'7p', b'7 dan pro'), (b'6p', b'6 dan pro'), (b'5p', b'5 dan pro'), (b'4p', b'4 dan pro'), (b'3p', b'3 dan pro'), (b'2p', b'2 dan pro'), (b'1p', b'1 dan pro'), (b'9d', b'9 dan'), (b'8d', b'8 dan'), (b'7d', b'7 dan'), (b'6d', b'6 dan'), (b'5d', b'5 dan'), (b'4d', b'4 dan'), (b'3d', b'3 dan'), (b'2d', b'2 dan'), (b'1d', b'1 dan'), (b'1k', b'1 kyu'), (b'2k', b'2 kyu'), (b'3k', b'3 kyu'), (b'4k', b'4 kyu'), (b'5k', b'5 kyu'), (b'6k', b'6 kyu'), (b'7k', b'7 kyu'), (b'8k', b'8 kyu'), (b'9k', b'9 kyu'), (b'10k', b'10 kyu'), (b'11k', b'11 kyu'), (b'12k', b'12 kyu'), (b'13k', b'13 kyu'), (b'14k', b'14 kyu'), (b'15k', b'15 kyu'), (b'16k', b'16 kyu'), (b'17k', b'17 kyu'), (b'18k', b'18 kyu'), (b'19k', b'19 kyu'), (b'20k', b'20 kyu')])),
                ('availability_review', models.CharField(default=b'weekly', max_length=10, choices=[(b'all', b'all'), (b'daily', b'daily'), (b'weekly', b'weekly'), (b'twoperweek', b'twoperweek'), (b'monthly', b'monthly')])),
                ('player', models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='match',
            name='black_player',
            field=models.ForeignKey(related_name='match_bplayer', to='go.Player'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='match',
            name='reviewer',
            field=models.ForeignKey(related_name='match_reviewers', to='go.Player', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='match',
            name='white_player',
            field=models.ForeignKey(related_name='match_wplayer', to='go.Player'),
            preserve_default=True,
        ),
    ]
