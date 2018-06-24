from os import getlogin
from pathlib import Path


# DT Format for log.
DT_FORMAT = "%Y%m%d_%H%M%S"
# Username used for log location.
USER = getlogin()
# Path of home.
PATH_HOME = Path(r'C:\Users\{0}\Desktop'.format(USER))
# Folder where data is stored.
FOLDER = r'logs'
# File where log is written to.
FILE = r'boot.log'
