# This settings.py file was generated by GitHub Copilot agent mode.

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# This settings.py file was generated by GitHub Copilot.

INSTALLED_APPS = [
    # ...existing apps...
    'octofit_tracker',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
