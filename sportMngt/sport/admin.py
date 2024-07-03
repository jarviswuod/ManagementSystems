from django.contrib import admin
from .models import User, Team, PlayerProfile, MatchEvent, Competition, Standings, Communication, Report, SystemAdmin
# Register your models here.User
admin.site.register(User)
admin.site.register(Team)
admin.site.register(PlayerProfile)
admin.site.register(MatchEvent)
admin.site.register(Competition)
admin.site.register(Standings)
admin.site.register(Communication)
admin.site.register(Report)
admin.site.register(SystemAdmin)
