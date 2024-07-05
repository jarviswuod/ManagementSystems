from django.contrib import admin
from .models import User, League, Team, Season, Game, TeamSeason, PlayerManager, TeamPlayerManager, SeasonPlayerManager, GamePlayerManager, Communication
# Register your models here

admin.site.register(User)
admin.site.register(League)
admin.site.register(Team)
admin.site.register(Season)
admin.site.register(Game)
admin.site.register(TeamSeason)
admin.site.register(PlayerManager)
admin.site.register(TeamPlayerManager)
admin.site.register(SeasonPlayerManager)
admin.site.register(GamePlayerManager)
admin.site.register(Communication)
