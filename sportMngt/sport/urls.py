
from . import views
from django.urls import path

urlpatterns = [
    path('user/', views.UserListCreateAPIView.as_view()),
    path('user/<int:pk>/', views.UserRetrieveAPIView.as_view()),
    path('user/<int:pk>/update/', views.UserUpdateAPIView.as_view()),
    path('user/<int:pk>/delete/', views.UserDestroyAPIView.as_view()),

    path('league/', views.LeagueListCreateAPIView.as_view()),
    path('league/<int:pk>/', views.LeagueRetrieveAPIView.as_view()),
    path('league/<int:pk>/update/', views.LeagueUpdateAPIView.as_view()),
    path('league/<int:pk>/delete/', views.LeagueDestroyAPIView.as_view()),

    path('team/', views.TeamListCreateAPIView.as_view()),
    path('team/<int:pk>/', views.TeamRetrieveAPIView.as_view()),
    path('team/<int:pk>/update/', views.TeamUpdateAPIView.as_view()),
    path('team/<int:pk>/delete/', views.TeamDestroyAPIView.as_view()),

    path('season/', views.SeasonListCreateAPIView.as_view()),
    path('season/<int:pk>/', views.SeasonRetrieveAPIView.as_view()),
    path('season/<int:pk>/update/', views.SeasonUpdateAPIView.as_view()),
    path('season/<int:pk>/delete/', views.SeasonDestroyAPIView.as_view()),

    path('game/', views.GameListCreateAPIView.as_view()),
    path('game/<int:pk>/', views.GameRetrieveAPIView.as_view()),
    path('game/<int:pk>/update/', views.GameUpdateAPIView.as_view()),
    path('game/<int:pk>/delete/', views.GameDestroyAPIView.as_view()),


    path('teamseason/', views.TeamSeasonListCreateAPIView.as_view()),
    path('teamseason/<int:pk>/', views.TeamSeasonRetrieveAPIView.as_view()),
    path('teamseason/<int:pk>/update/', views.TeamSeasonUpdateAPIView.as_view()),
    path('teamseason/<int:pk>/delete/', views.TeamSeasonDestroyAPIView.as_view()),


    path('playermanager/', views.PlayerManagerListCreateAPIView.as_view()),
    path('playermanager/<int:pk>/', views.PlayerManagerRetrieveAPIView.as_view()),
    path('playermanager/<int:pk>/update/',
         views.PlayerManagerUpdateAPIView.as_view()),
    path('playermanager/<int:pk>/delete/',
         views.PlayerManagerDestroyAPIView.as_view()),

    path('team_contract/', views.TeamPlayerManagerListCreateAPIView.as_view()),
    path('team_contract/<int:pk>/',
         views.TeamPlayerManagerRetrieveAPIView.as_view()),
    path('team_contract/<int:pk>/update/',
         views.TeamPlayerManagerUpdateAPIView.as_view()),
    path('team_contract/<int:pk>/delete/',
         views.TeamPlayerManagerDestroyAPIView.as_view()),


    path('season_contract/',
         views.SeasonPlayerManagerListCreateAPIView.as_view()),
    path('season_contract/<int:pk>/',
         views.SeasonPlayerManagerRetrieveAPIView.as_view()),
    path('season_contract/<int:pk>/update/',
         views.SeasonPlayerManagerUpdateAPIView.as_view()),
    path('season_contract/<int:pk>/delete/',
         views.SeasonPlayerManagerDestroyAPIView.as_view()),


    path('game_events/', views.GamePlayerManagerListCreateAPIView.as_view()),
    path('game_events/<int:pk>/',
         views.GamePlayerManagerRetrieveAPIView.as_view()),
    path('game_events/<int:pk>/update/',
         views.GamePlayerManagerUpdateAPIView.as_view()),
    path('game_events/<int:pk>/delete/',
         views.GamePlayerManagerDestroyAPIView.as_view()),


    path('communication/', views.CommunicationListCreateAPIView.as_view()),
    path('communication/<int:pk>/', views.CommunicationRetrieveAPIView.as_view()),
    path('communication/<int:pk>/update/',
         views.CommunicationUpdateAPIView.as_view()),
    path('communication/<int:pk>/delete/',
         views.CommunicationDestroyAPIView.as_view()),
]
