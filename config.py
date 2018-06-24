from os import getlogin
from pathlib import Path


# Username used for log location.
USER = getlogin()
# Path of home.
PATH = Path(r'C:\Users\{0}\Desktop'.format(USER))
# Folder where data is stored.
FOLDER = r'logs'
# File where log is written to.
FILE = r'boot.log'
