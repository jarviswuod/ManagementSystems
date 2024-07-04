from django.contrib import admin
from . import models
# Register your models here.User
admin.site.register(models.User)
admin.site.register(models.League)
admin.site.register(models.Team)
admin.site.register(models.Season)
admin.site.register(models.Game)
admin.site.register(models.TeamSeason)
admin.site.register(models.PlayerManager)
admin.site.register(models.TeamPlayerManager)
admin.site.register(models.SeasonPlayerManager)
admin.site.register(models.Communication)
