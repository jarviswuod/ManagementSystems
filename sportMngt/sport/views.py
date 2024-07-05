from rest_framework import generics

from .models import User, League, Team, Season, Game, TeamSeason, PlayerManager, TeamPlayerManager, SeasonPlayerManager, GamePlayerManager, Communication

from .serializers import UserSerializer, LeagueSerializer, TeamSerializer, CommunicationSerializer

# Create your views here.


# USER

class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


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

# COMMUNICATION


class CommunicationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Communication.objects.all()
    serializer_class = CommunicationSerializer


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
