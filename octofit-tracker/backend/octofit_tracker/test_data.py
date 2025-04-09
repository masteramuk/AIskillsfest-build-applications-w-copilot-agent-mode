# Test data for populating the octofit_db database

test_data = {
    "users": [
        {"id": 1, "email": "john.doe@example.com", "name": "John Doe"},
        {"id": 2, "email": "jane.smith@example.com", "name": "Jane Smith"}
    ],
    "teams": [
        {"id": 1, "name": "Team A"},
        {"id": 2, "name": "Team B"}
    ],
    "activities": [
        {"user_id": 1},
        {"user_id": 2}
    ],
    "leaderboard": [
        {"team_id": 1},
        {"team_id": 2}
    ],
    "workouts": [
        {"name": "Morning Run"},
        {"name": "Evening Yoga"}
    ]
}
