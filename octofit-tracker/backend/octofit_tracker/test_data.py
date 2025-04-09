# Test data for the Octofit app

test_users = [
    {"email": "john.doe@example.com", "name": "John Doe", "password": "password123"},
    {"email": "jane.smith@example.com", "name": "Jane Smith", "password": "password123"},
    {"email": "alice.jones@example.com", "name": "Alice Jones", "password": "password123"},
]

test_teams = [
    {"name": "Team Alpha", "members": ["john.doe@example.com", "jane.smith@example.com"]},
    {"name": "Team Beta", "members": ["alice.jones@example.com"]},
]

test_activities = [
    {"name": "Running", "calories_burned": 300},
    {"name": "Cycling", "calories_burned": 250},
]

test_leaderboard = [
    {"user": "john.doe@example.com", "score": 100},
    {"user": "jane.smith@example.com", "score": 80},
]

test_workouts = [
    {"name": "Morning Run", "duration": 30, "activity": "Running"},
    {"name": "Evening Cycle", "duration": 45, "activity": "Cycling"},
]
