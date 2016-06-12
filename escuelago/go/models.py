from django.contrib.auth.models import User
from django.db import models

RANKS = (
        ('9p', '9 dan pro'),
        ('8p', '8 dan pro'),
        ('7p', '7 dan pro'),
        ('6p', '6 dan pro'),
        ('5p', '5 dan pro'),
        ('4p', '4 dan pro'),
        ('3p', '3 dan pro'),
        ('2p', '2 dan pro'),
        ('1p', '1 dan pro'),
        ('9d', '9 dan'),
        ('8d', '8 dan'),
        ('7d', '7 dan'),
        ('6d', '6 dan'),
        ('5d', '5 dan'),
        ('4d', '4 dan'),
        ('3d', '3 dan'),
        ('2d', '2 dan'),
        ('1d', '1 dan'),
        ('1k', '1 kyu'),
        ('2k', '2 kyu'),
        ('3k', '3 kyu'),
        ('4k', '4 kyu'),
        ('5k', '5 kyu'),
        ('6k', '6 kyu'),
        ('7k', '7 kyu'),
        ('8k', '8 kyu'),
        ('9k', '9 kyu'),
        ('10k', '10 kyu'),
        ('11k', '11 kyu'),
        ('12k', '12 kyu'),
        ('13k', '13 kyu'),
        ('14k', '14 kyu'),
        ('15k', '15 kyu'),
        ('16k', '16 kyu'),
        ('17k', '17 kyu'),
        ('18k', '18 kyu'),
        ('19k', '19 kyu'),
        ('20k', '20 kyu')
)

STATUS = (
        ('waiting', 'waiting'),
        ('reviewing', 'reviewing'),
        ('reviewed', 'reviewed')
)

AVAILABILITY = (
        ('all', 'all'),
        ('daily', 'daily'),
        ('weekly', 'weekly'),
        ('twoperweek', 'twoperweek'),
        ('monthly', 'monthly'),
)


class Player(models.Model):
    player = models.OneToOneField(User)
    current_rank = models.CharField(max_length=3, choices=RANKS, default='20k')
    availability_review = models.CharField(max_length=10, choices=AVAILABILITY, default='weekly')


class Match(models.Model):
    black_player = models.ForeignKey(Player, related_name='match_bplayer')
    black_rank = models.CharField(max_length=3, choices=RANKS, default='20k')
    white_player = models.ForeignKey(Player, related_name='match_wplayer')
    white_rank = models.CharField(max_length=3, choices=RANKS, default='20k')
    handicap = models.IntegerField(blank=True, null=True)
    reviewer = models.ForeignKey(Player, related_name='match_reviewers', null=True)
    reviewer_rank = models.CharField(max_length=3, choices=RANKS, default='20k')
    sgf = models.CharField(max_length=2048)
    status = models.CharField(max_length=3, choices=RANKS, default='20k')
    upload_day = models.DateField(help_text="Format: 'DD/MM/YYYY'", auto_now=True)
    comments = models.CharField(max_length=3, choices=RANKS, default='20k')
