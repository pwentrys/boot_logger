import os
import pathlib
from text import Text
from config import FILE, FOLDER, PATH_HOME


def run():
    """
    Runs logging.
    :return:
    """
    # Sanity for base directory.
    assert PATH_HOME.exists(), exit(1)

    PATH_LOGS = pathlib.Path(os.path.join(str(PATH_HOME), FOLDER))

    # Create logs folder if not exists.
    if not PATH_LOGS.exists():
        os.mkdir(str(PATH_LOGS))
        assert PATH_LOGS.exists(), exit(2)

    # Log file path.
    PATH_FILE = pathlib.Path(os.path.join(str(PATH_LOGS), FILE))

    # Text obj.
    t = Text(PATH_FILE)
    print('SUCCESS') if t.execute() else print('FAIL')


if __name__ == '__main__':
    try:
        run()
    except Exception as err:
        print(err)
