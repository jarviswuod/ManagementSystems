from django.db import models


class User(models.Model):
    USER_TYPES = [
        ('Admin', 'Admin'),
        ('Player', 'Player'),
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, null=True)
    user_type = models.CharField(max_length=7, choices=USER_TYPES)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_modified = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

class League(models.Model):
    created_by = models.ForeignKey(
        "sport.User", related_name='created_by', on_delete=models.SET_NULL, null=True, blank=True)
    id=models.AutoField()
    name=models.CharField(max_length=255)
    founded=models.DateField()
    country=models.CharField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_modified = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name


class Team(models.Model):
    created_by = models.ForeignKey(
        "sport.User", related_name='created_by', on_delete=models.SET_NULL, null=True, blank=True)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    founded=models.DateField()
    coach = models.CharField(max_length=255)
    ground = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_modified = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

class Season(models.Model):
    created_by = models.ForeignKey(
        "sport.User", related_name='created_by', on_delete=models.SET_NULL, null=True, blank=True)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255) # 2024/2025
    league_id = models.ForeignKey("sport.League", on_delete=models.CASCADE)
    number = models.IntegerField()
    start_date= models.DateField()
    end_date= models.DateField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_modified = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name


class Game(models.Model):
    id = models.AutoField(primary_key=True)
    created_by = models.ForeignKey(
        "sport.User", related_name='created_by', on_delete=models.SET_NULL, null=True, blank=True)
    id = models.AutoField(primary_key=True)
    home_team_id = models.ForeignKey(
        "sport.Team", related_name='team1', on_delete=models.CASCADE)
    away_team_id = models.ForeignKey(
        "sport.Team", related_name='team2', on_delete=models.CASCADE)
    league_id = models.ForeignKey(
        "sport.League", related_name='league', on_delete=models.CASCADE)
    date = models.DateTimeField()
    start_time= models.models.DateTimeField()
    end_time= models.models.DateTimeField()
    location = models.CharField(max_length=255)
    home_team_score = models.IntegerField(null=True)
    away_team_score = models.IntegerField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_modified = models.DateTimeField(auto_now=True, null=True)
    is_played=models.BooleanField(null=True)
    

    def __str__(self):
        return f"{self.home_team_id.name} vs {self.away_team_id.name}  {self.league_id.name} at {self.date}"

class TeamSeason(models.Model):
    id = models.AutoField(primary_key=True)
    season_id=models.ForeignKey("sport.Season", null=True)
    team_id=models.ForeignKey("sport.Team", null=True)
    point=models.IntegerField(null=True)
    def __str__(self):
        return f"{self.team_id.name} vs {self.season_id.name} at {self.point}"


class PlayerManager(models.Model):
    GENDER = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Prefer not to say', 'Prefer not to say'),
    ]
    id = models.AutoField(primary_key=True)
    user_id = models.OneToOneField(
        "sport.User", on_delete=models.CASCADE, primary_key=True, limit_choices_to={'UserType': 'Player'})
    # team_id = models.ForeignKey("sport.Team", on_delete=models.SET_NULL, null=True)
    date_of_birth = models.DateTime()
    gender = models.CharField(max_length=25, choices=GENDER)
    salary=models.IntegerField(null=True)
    jersey_no=models.IntegerField(null=True)
    # position = models.ForeignKey(
    #     "sport.Position", related_name='position', on_delete=models.CASCADE)
    position = models.TextField(null=True)
    # performance_stats = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_modified = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.user_id.name


class Team_PlayerManager(models.Model):
    id = models.AutoField(primary_key=True)
    player_id = models.ForeignKey("sport.PlayerManager", on_delete=models.CASCADE)
    team_id = models.ForeignKey("sport.Team", on_delete=models.CASCADE)
    start_date=models.DateField(null=True)
    end_date=models.DateField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_modified = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.player_id.user_id.name}"

class Season_PlayerManager(models.Model):
    id = models.AutoField(primary_key=True)
    manager_id = models.ForeignKey("sport.PlayerManager", on_delete=models.CASCADE)
    team_id = models.ForeignKey("sport.Team", on_delete=models.CASCADE)
    start_date=models.DateField(null=True)
    end_date=models.DateField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_modified = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.player_id.user_id.name}"


# class Competition(models.Model):
#     created_by = models.ForeignKey(
#         "sport.User", related_name='created_by', on_delete=models.SET_NULL, null=True, blank=True)
#     competition_id = models.AutoField(primary_key=True)
#     competition_name = models.CharField(max_length=255)
#     start_date = models.DateField()
#     end_date = models.DateField()
#     status = models.CharField(max_length=255)
#     no_of_teams = models.IntegerField()
#     date_created = models.DateTimeField(auto_now_add=True, null=True)
#     date_modified = models.DateTimeField(auto_now=True, null=True)

#     def __str__(self):
#         return self.competition_name




# class Standings(models.Model):
#     standing_id = models.AutoField(primary_key=True)
#     competition_id = models.ForeignKey("sport.Competition", on_delete=models.CASCADE)
#     team_id = models.ForeignKey("sport.Team", on_delete=models.CASCADE)
#     points = models.IntegerField()
#     date_created = models.DateTimeField(auto_now_add=True, null=True)
#     date_modified = models.DateTimeField(auto_now=True, null=True)

#     def __str__(self):
#         return f"{self.team_id} - {self.points} Points"


class Communication(models.Model):
    writer = models.ForeignKey(
        "sport.User", related_name='writer', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"From {self.writer} at {self.timestamp}"


# class Report(models.Model):
#     user = models.ForeignKey("sport.User", on_delete=models.CASCADE)
#     report_type = models.CharField(max_length=100)
#     report_content = models.TextField()
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.report_type} by {self.user}"


# class SystemAdmin(models.Model):
#     user = models.OneToOneField(
#         "sport.User", on_delete=models.CASCADE, primary_key=True)
#     role = models.CharField(max_length=100)
#     date_created = models.DateTimeField(auto_now_add=True, null=True)
#     date_modified = models.DateTimeField(auto_now=True, null=True)

#     def __str__(self):
#         return f"{self.user} - {self.role}"
