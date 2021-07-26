# Define your variable in this file
import os.path

MAIN_DIR = os.path.dirname(os.path.dirname(__file__))

LOG_FILENAME = os.path.join(MAIN_DIR, 'app_logs.log')        # Where write the logs
DATABASE_FILENAME = os.path.join(MAIN_DIR, 'chess_db.json')  # Where store data

VERSION = "2021.07.26"

