from django.core.management.base import BaseCommand
from octofit_tracker.test_data import test_data
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Populate users
        for user_data in test_data['users']:
            User.objects.get_or_create(**user_data)

        # Populate teams
        for team_data in test_data['teams']:
            Team.objects.get_or_create(**team_data)

        # Populate activities
        for activity_data in test_data['activities']:
            Activity.objects.get_or_create(**activity_data)

        # Populate leaderboard
        for leaderboard_data in test_data['leaderboard']:
            Leaderboard.objects.get_or_create(**leaderboard_data)

        # Populate workouts
        for workout_data in test_data['workouts']:
            Workout.objects.get_or_create(**workout_data)

        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))
