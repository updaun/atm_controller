from config import LOGGER
from datetime import datetime


class Logger:
    def logging(self, action, user="anonymous", log_level="INFO"):
        now = datetime.now()
        with open(LOGGER["LOGGER_DIR"], "a") as f:
            f.write(f"{log_level} | {now} | {user} | {action}\n")
