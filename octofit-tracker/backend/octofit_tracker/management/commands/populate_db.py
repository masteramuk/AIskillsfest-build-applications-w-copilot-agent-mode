from django.core.management.base import BaseCommand
from octofit_tracker.test_data import test_users, test_teams, test_activities, test_leaderboard, test_workouts
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Populate users
        for user_data in test_users:
            User.objects.create(**user_data)

        # Populate teams
        for team_data in test_teams:
            team = Team.objects.create(name=team_data['name'])
            for email in team_data['members']:
                user = User.objects.get(email=email)
                team.members.add(user)

        # Populate activities
        for activity_data in test_activities:
            user = User.objects.get(email=activity_data['user'])
            Activity.objects.create(user=user, **{k: v for k, v in activity_data.items() if k != 'user'})

        # Populate leaderboard
        for leaderboard_data in test_leaderboard:
            team = Team.objects.get(name=leaderboard_data['team'])
            Leaderboard.objects.create(team=team, points=leaderboard_data['points'])

        # Populate workouts
        for workout_data in test_workouts:
            Workout.objects.create(**workout_data)

        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))
