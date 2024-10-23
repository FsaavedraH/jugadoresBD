from django.urls import path
from .views import player_view, team_view, api_root

urlpatterns = [
    path('', api_root, name='api_root'),
    path('players/', player_view, name='players'),
    path('players/<str:player_id>/', player_view, name='player-detail'),  # Cambia a <str:player_id>
    path('teams/', team_view, name='teams'),
    path('teams/<slug:team_id>/', team_view, name='team-detail'),  # Cambia a <slug:team_id>
]
