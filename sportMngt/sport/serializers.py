from rest_framework import serializers
from .models import User, League, Team, Season, Game, TeamSeason, PlayerManager, TeamPlayerManager, SeasonPlayerManager, GamePlayerManager, Communication


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class LeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = '__all__'


class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class SeasonSerializer(serializers.ModelSerializer):
    # league_id = LeagueSerializer()

    class Meta:
        model = Season
        fields = '__all__'


class GameSerializer(serializers.ModelSerializer):
    home_team_id = TeamSerializer()
    away_team_id = TeamSerializer()
    season_id = SeasonSerializer()

    class Meta:
        model = Game
        fields = '__all__'


class TeamSeasonSerializer(serializers.ModelSerializer):
    season_id = SeasonSerializer()
    team_id = TeamSerializer()

    class Meta:
        model = TeamSeason
        fields = '__all__'


class PlayerManagerSerializer(serializers.ModelSerializer):

    class Meta:
        model = PlayerManager
        fields = '__all__'


class TeamPlayerManagerSerializer(serializers.ModelSerializer):
    # player_or_manager_id = PlayerManagerSerializer()
    # team_id = TeamSerializer()

    class Meta:
        model = TeamPlayerManager
        fields = '__all__'


class SeasonPlayerManagerSerializer(serializers.ModelSerializer):
    # manager_id = PlayerManagerSerializer()
    # season_id = SeasonSerializer()

    class Meta:
        model = SeasonPlayerManager
        fields = '__all__'


class GamePlayerManagerSerializer(serializers.ModelSerializer):
    # player_or_manager_id = PlayerManagerSerializer()
    # game_id = GameSerializer()

    class Meta:
        model = GamePlayerManager
        fields = '__all__'


class CommunicationSerializer(serializers.ModelSerializer):
    writer_id = UserSerializer()

    class Meta:
        model = Communication
        fields = '__all__'
