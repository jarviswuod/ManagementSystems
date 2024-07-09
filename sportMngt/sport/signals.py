from django.db.models import Q
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Game, TeamSeason


@receiver(post_save, sender=Game)
def update_team_season_stats(sender, instance, **kwargs):
    print(11111111)
    print(22222222)
    print(33333333)
    if instance.is_played:
        # Determine the outcome for each team
        home_win = instance.home_team_score > instance.away_team_score
        away_win = instance.away_team_score > instance.home_team_score
        draw = instance.home_team_score == instance.away_team_score

        # Update the home team stats
        home_team_season, created = TeamSeason.objects.get_or_create(
            season_id=instance.season_id, team_id=instance.home_team_id,
            defaults={'points': 0, 'wins': 0,
                      'draws': 0, 'lost': 0, 'games_played': 0}
        )
        if not created:
            home_team_season.games_played = Game.objects.filter(
                Q(home_team_id=instance.home_team_id) | Q(
                    away_team_id=instance.home_team_id),
                season_id=instance.season_id,
                is_played=True
            ).count()

            if home_win:
                home_team_season.wins += 1
                home_team_season.points += 3
            elif draw:
                home_team_season.draws += 1
                home_team_season.points += 1
            else:
                home_team_season.lost += 1
            home_team_season.save()

            print(f'${home_team_season}')
            print(f'${home_team_season}')
            print(f'${home_team_season}')

        # Update the away team stats
        away_team_season, created = TeamSeason.objects.get_or_create(
            season_id=instance.season_id, team_id=instance.away_team_id,
            defaults={'points': 0, 'wins': 0,
                      'draws': 0, 'lost': 0, 'games_played': 0}
        )
        if not created:
            away_team_season.games_played = Game.objects.filter(
                Q(home_team_id=instance.away_team_id) | Q(
                    away_team_id=instance.away_team_id),
                season_id=instance.season_id,
                is_played=True
            ).count()

            if away_win:
                away_team_season.wins += 1
                away_team_season.points += 3
            elif draw:
                away_team_season.draws += 1
                away_team_season.points += 1
            else:
                away_team_season.lost += 1
            away_team_season.save()

            print(f'${away_team_season}')
            print(f'${away_team_season}')
            print(f'${away_team_season}')
