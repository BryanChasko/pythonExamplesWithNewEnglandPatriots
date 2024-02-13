# Description: This file contains a custom logging configuration that adds color coding to log levels.
# for quick re-use in our projects

from logging import basicConfig, INFO, info, Formatter, StreamHandler, getLogger, record
from sys import stdout

# Add color coding to log levels
class ColorFormatter(Formatter):
    def format(self, record):
        levelname = record.levelname
        if levelname == 'DEBUG':
            # Set levelname to blue
            record.levelname = '\033[94m' + levelname + '\033[0m'  # Blue
        elif levelname == 'INFO':
            # Set levelname to green
            record.levelname = '\033[92m' + levelname + '\033[0m'  # Green
        elif levelname == 'WARNING':
            # Set levelname to yellow
            record.levelname = '\033[93m' + levelname + '\033[0m'  # Yellow
        elif levelname == 'ERROR':
            # Set levelname to red
            record.levelname = '\033[91m' + levelname + '\033[0m'  # Red
        elif levelname == 'CRITICAL':
            # Set levelname to magenta
            record.levelname = '\033[95m' + levelname + '\033[0m'  # Magenta
        return super().format(record)

# Create a StreamHandler with color formatting
def setup_logging():
    getLogger().setLevel(INFO)
    ColorFormatter.format('%(asctime)s - %(levelname)s - %(message)s')
    handler = StreamHandler(stdout)
    handler.setFormatter(ColorFormatter())
    return handler

# set up the logger when the module is imported by another file
setup_logging()