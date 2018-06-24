from sys import platform
from pathlib import Path


# DT Format for log.
DT_FORMAT = "%Y%m%d_%H%M%S"

# Determine path for home.
if platform == 'win32':
    from os import getlogin

    # Username used for log location.
    USER = getlogin()
    PATH_HOME = Path(r'C:\Users\{0}\Desktop'.format(USER))
elif platform == 'linux' or platform == 'darwin':
    import pwd
    from os import getuid

    USER = pwd.getpwuid(getuid())[0]
    PATH_HOME = Path(r'/home/{0}/'.format(USER))
else:
    print(platform)
    exit(5)

# Folder where data is stored.
FOLDER = r'logs'
# File where log is written to.
FILE = r'boot.log'
