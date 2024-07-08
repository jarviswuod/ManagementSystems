from rest_framework import generics

from .models import User, League, Team, Season, Game, TeamSeason, PlayerManager, TeamPlayerManager, SeasonPlayerManager, GamePlayerManager, Communication

from .serializers import UserSerializer, LeagueSerializer, TeamSerializer, SeasonSerializer, GameSerializer, TeamSeasonSerializer, PlayerManagerSerializer, TeamPlayerManagerSerializer,  SeasonPlayerManagerSerializer, GamePlayerManagerSerializer, CommunicationSerializer


# USER

class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'


class UserUpdateAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()


class UserDestroyAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


# LEAGUE


class LeagueListCreateAPIView(generics.ListCreateAPIView):
    queryset = League.objects.all()
    serializer_class = LeagueSerializer


class LeagueRetrieveAPIView(generics.RetrieveAPIView):
    queryset = League.objects.all()
    serializer_class = LeagueSerializer
    lookup_field = 'pk'


class LeagueUpdateAPIView(generics.UpdateAPIView):
    queryset = League.objects.all()
    serializer_class = LeagueSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()


class LeagueDestroyAPIView(generics.DestroyAPIView):
    queryset = League.objects.all()
    serializer_class = LeagueSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


# TEAM


class TeamListCreateAPIView(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TeamRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    lookup_field = 'pk'


class TeamUpdateAPIView(generics.UpdateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()


class TeamDestroyAPIView(generics.DestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


# SEASON


class SeasonListCreateAPIView(generics.ListCreateAPIView):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer


class SeasonRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer
    lookup_field = 'pk'


class SeasonUpdateAPIView(generics.UpdateAPIView):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()


class SeasonDestroyAPIView(generics.DestroyAPIView):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)

# GAME


class GameListCreateAPIView(generics.ListCreateAPIView):
    queryset = Game.objects.all().order_by('-date')
    serializer_class = GameSerializer


class GameRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    lookup_field = 'pk'


class GameUpdateAPIView(generics.UpdateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()


class GameDestroyAPIView(generics.DestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


# TEAMSEASON


class TeamSeasonListCreateAPIView(generics.ListCreateAPIView):
    queryset = TeamSeason.objects.all().order_by('-points')
    serializer_class = TeamSeasonSerializer


class TeamSeasonRetrieveAPIView(generics.RetrieveAPIView):
    queryset = TeamSeason.objects.all()
    serializer_class = TeamSeasonSerializer
    lookup_field = 'pk'


class TeamSeasonUpdateAPIView(generics.UpdateAPIView):
    queryset = TeamSeason.objects.all()
    serializer_class = TeamSeasonSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()


class TeamSeasonDestroyAPIView(generics.DestroyAPIView):
    queryset = TeamSeason.objects.all()
    serializer_class = TeamSeasonSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


# PLAYERMANAGER


class PlayerManagerListCreateAPIView(generics.ListCreateAPIView):
    queryset = PlayerManager.objects.all()
    serializer_class = PlayerManagerSerializer


class PlayerManagerRetrieveAPIView(generics.RetrieveAPIView):
    queryset = PlayerManager.objects.all()
    serializer_class = PlayerManagerSerializer
    lookup_field = 'pk'


class PlayerManagerUpdateAPIView(generics.UpdateAPIView):
    queryset = PlayerManager.objects.all()
    serializer_class = PlayerManagerSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()


class PlayerManagerDestroyAPIView(generics.DestroyAPIView):
    queryset = PlayerManager.objects.all()
    serializer_class = PlayerManagerSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


# TEAMPLAYERMANAGER


class TeamPlayerManagerListCreateAPIView(generics.ListCreateAPIView):
    queryset = TeamPlayerManager.objects.all()
    serializer_class = TeamPlayerManagerSerializer


class TeamPlayerManagerRetrieveAPIView(generics.RetrieveAPIView):
    queryset = TeamPlayerManager.objects.all()
    serializer_class = TeamPlayerManagerSerializer
    lookup_field = 'pk'


class TeamPlayerManagerUpdateAPIView(generics.UpdateAPIView):
    queryset = TeamPlayerManager.objects.all()
    serializer_class = TeamPlayerManagerSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()


class TeamPlayerManagerDestroyAPIView(generics.DestroyAPIView):
    queryset = TeamPlayerManager.objects.all()
    serializer_class = TeamPlayerManagerSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


# SEASONPLAYERMANAGER


class SeasonPlayerManagerListCreateAPIView(generics.ListCreateAPIView):
    queryset = SeasonPlayerManager.objects.all()
    serializer_class = SeasonPlayerManagerSerializer


class SeasonPlayerManagerRetrieveAPIView(generics.RetrieveAPIView):
    queryset = SeasonPlayerManager.objects.all()
    serializer_class = SeasonPlayerManagerSerializer
    lookup_field = 'pk'


class SeasonPlayerManagerUpdateAPIView(generics.UpdateAPIView):
    queryset = SeasonPlayerManager.objects.all()
    serializer_class = SeasonPlayerManagerSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()


class SeasonPlayerManagerDestroyAPIView(generics.DestroyAPIView):
    queryset = SeasonPlayerManager.objects.all()
    serializer_class = SeasonPlayerManagerSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


# GAMEPLAYERMANAGER


class GamePlayerManagerListCreateAPIView(generics.ListCreateAPIView):
    queryset = GamePlayerManager.objects.all()
    serializer_class = GamePlayerManagerSerializer


class GamePlayerManagerRetrieveAPIView(generics.RetrieveAPIView):
    queryset = GamePlayerManager.objects.all()
    serializer_class = GamePlayerManagerSerializer
    lookup_field = 'pk'


class GamePlayerManagerUpdateAPIView(generics.UpdateAPIView):
    queryset = GamePlayerManager.objects.all()
    serializer_class = GamePlayerManagerSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()


class GamePlayerManagerDestroyAPIView(generics.DestroyAPIView):
    queryset = GamePlayerManager.objects.all()
    serializer_class = GamePlayerManagerSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


# COMMUNICATION


class CommunicationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Communication.objects.all().order_by('-timestamp')
    serializer_class = CommunicationSerializer


class CommunicationRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Communication.objects.all()
    serializer_class = CommunicationSerializer
    lookup_field = 'pk'


class CommunicationUpdateAPIView(generics.UpdateAPIView):
    queryset = Communication.objects.all()
    serializer_class = CommunicationSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()


class CommunicationDestroyAPIView(generics.DestroyAPIView):
    queryset = Communication.objects.all()
    serializer_class = CommunicationSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)
