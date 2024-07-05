
from . import views
from django.urls import path

urlpatterns = [
    path('user/', views.UserListCreateAPIView.as_view()),
    path('user/<int:pk>/update/', views.UserUpdateAPIView.as_view()),
    path('user/<int:pk>/delete/', views.UserDestroyAPIView.as_view()),

    path('league/', views.LeagueListCreateAPIView.as_view()),
    path('league/<int:pk>/update/', views.LeagueUpdateAPIView.as_view()),
    path('league/<int:pk>/delete/', views.LeagueDestroyAPIView.as_view()),

    path('team/', views.TeamListCreateAPIView.as_view()),
    path('team/<int:pk>/update/', views.TeamUpdateAPIView.as_view()),
    path('team/<int:pk>/delete/', views.TeamDestroyAPIView.as_view()),

    path('communication/', views.CommunicationListCreateAPIView.as_view()),
    path('communication/<int:pk>/update/',
         views.CommunicationUpdateAPIView.as_view()),
    path('communication/<int:pk>/delete/',
         views.CommunicationDestroyAPIView.as_view()),


]
