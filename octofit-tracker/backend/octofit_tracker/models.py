from djongo import models

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=128)  # Add a field for storing hashed passwords

class Team(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField('User', related_name='teams')  # Add a many-to-many relationship to the User model

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)  # Add a name field for the activity
    calories_burned = models.IntegerField(default=0)  # Provide a default value for the calories_burned field

class Leaderboard(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Add a user field to associate with a User
    score = models.IntegerField(default=0)  # Provide a valid default value for the score field

class Workout(models.Model):
    name = models.CharField(max_length=255)
    duration = models.IntegerField()  # Add a duration field for the workout
    activity = models.CharField(max_length=255)  # Add an activity field for the workout
