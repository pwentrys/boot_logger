from os import getlogin
from sys import platform
from pathlib import Path


# DT Format for log.
DT_FORMAT = "%Y%m%d_%H%M%S"
# Username used for log location.
USER = getlogin()

# Path of home.
if platform is 'win32':
    PATH_HOME = Path(r'C:\Users\{0}\Desktop'.format(USER))
elif platform is 'linux' or platform is 'darwin':
    PATH_HOME = Path(r'/home/{0}/'.format(USER))

# Folder where data is stored.
FOLDER = r'logs'
# File where log is written to.
FILE = r'boot.log'
