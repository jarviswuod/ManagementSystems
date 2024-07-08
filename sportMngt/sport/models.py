from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.first_name


class League(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    founded = models.DateField(null=True)
    country = models.CharField(null=True)
    number_of_teams = models.IntegerField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Team(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    founded = models.DateField()
    number_of_players = models.IntegerField()
    ground = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Season(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)  # 2024/2025
    league_id = models.ForeignKey("sport.League", on_delete=models.CASCADE)
    number_of_teams = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Game(models.Model):
    id = models.AutoField(primary_key=True)
    home_team_id = models.ForeignKey(
        "sport.Team", related_name='home_team_id', on_delete=models.CASCADE)
    away_team_id = models.ForeignKey(
        "sport.Team", related_name='away_team_id', on_delete=models.CASCADE)
    season_id = models.ForeignKey(
        "sport.Season",  on_delete=models.CASCADE)
    date = models.DateField(null=True)
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    location = models.CharField(max_length=255)
    home_team_score = models.IntegerField(null=True)
    away_team_score = models.IntegerField(null=True)
    is_played = models.BooleanField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.home_team_id.name} vs {self.away_team_id.name}  {self.season_id.name} at {self.start_time}"


class TeamSeason(models.Model):
    id = models.AutoField(primary_key=True)
    season_id = models.ForeignKey(
        "sport.Season", on_delete=models.SET_NULL, null=True)
    team_id = models.ForeignKey(
        "sport.Team", on_delete=models.SET_NULL, null=True)
    points = models.IntegerField(null=True)
    wins = models.IntegerField(null=True)
    draws = models.IntegerField(null=True)
    lost = models.IntegerField(null=True)
    games_played = models.IntegerField(default=0, null=True)

    def __str__(self):
        return f"{self.team_id.name} in {self.season_id.name} at {self.points}"


class PlayerManager(models.Model):
    GENDER = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Prefer not to say', 'Prefer not to say'),
    ]
    ROLE = [
        ('Player', 'Player'),
        ('Manager', 'Manager'),
    ]
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=255, null=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=25, choices=GENDER)
    salary = models.IntegerField(null=True)
    jersey_no = models.IntegerField(null=True)
    position = models.TextField(null=True)
    role = models.CharField(max_length=25, choices=ROLE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class TeamPlayerManager(models.Model):
    id = models.AutoField(primary_key=True)
    player_or_manager_id = models.ForeignKey(
        "sport.PlayerManager", on_delete=models.CASCADE)
    team_id = models.ForeignKey("sport.Team", on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.player_or_manager_id.first_name} in {self.team_id}"


class SeasonPlayerManager(models.Model):
    id = models.AutoField(primary_key=True)
    manager_id = models.ForeignKey(
        "sport.PlayerManager", on_delete=models.CASCADE)
    season_id = models.ForeignKey("sport.Season", on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.manager_id.first_name}"


class GamePlayerManager(models.Model):
    EVENT = [
        ('Goal', 'Goal'),
        ('Substitute', 'Substitute'),
        ('Yellow Card', 'Yellow Card'),
        ('Read Card', 'Read Card'),
    ]
    id = models.AutoField(primary_key=True)
    player_or_manager_id = models.ForeignKey(
        "sport.PlayerManager", on_delete=models.CASCADE)
    game_id = models.ForeignKey("sport.Game", on_delete=models.CASCADE)
    event = models.CharField(max_length=25, choices=EVENT)
    time = models.CharField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.player_or_manager_id.first_name}"


class Communication(models.Model):
    id = models.AutoField(primary_key=True)
    writer_id = models.ForeignKey(
        "sport.User", related_name='writer', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"From {self.writer_id} at {self.timestamp}"
