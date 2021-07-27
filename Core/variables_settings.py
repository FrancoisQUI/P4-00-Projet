# Define your variable in this file
import os.path

MAIN_DIR = os.path.dirname(os.path.dirname(__file__))

# Where write the logs
LOG_FILENAME = os.path.join(MAIN_DIR, 'app_logs.log')
# Where store data
DATABASE_FILENAME = os.path.join(MAIN_DIR, 'chess_db.json')

# App version
VERSION = "2021.07.27"
