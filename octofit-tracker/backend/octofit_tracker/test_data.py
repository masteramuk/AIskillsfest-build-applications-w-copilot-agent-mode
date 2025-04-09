# Test data for the OctoFit app

test_users = [
    {"email": "john@example.com", "name": "John Doe"},
    {"email": "jane@example.com", "name": "Jane Smith"},
]

test_teams = [
    {"name": "Team Alpha", "members": ["john@example.com", "jane@example.com"]},
    {"name": "Team Beta", "members": []},
]

test_activities = [
    {"user": "john@example.com", "activity": "Running", "duration": 30, "calories_burned": 300},
    {"user": "jane@example.com", "activity": "Cycling", "duration": 45, "calories_burned": 400},
]

test_leaderboard = [
    {"team": "Team Alpha", "points": 700},
    {"team": "Team Beta", "points": 0},
]

test_workouts = [
    {"name": "Morning Run", "description": "A quick 5km run to start the day", "duration": 30},
    {"name": "Evening Yoga", "description": "Relaxing yoga session", "duration": 60},
]
