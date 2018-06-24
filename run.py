import os
import pathlib
from datetime import datetime
from config import DT_FORMAT, FILE, FOLDER, PATH_HOME


# Sanity for base directory.
assert PATH_HOME.exists(), exit(1)

PATH_LOGS = pathlib.Path(os.path.join(str(PATH_HOME), FOLDER))

# Create logs folder if not exists.
if not PATH_LOGS.exists():
    os.mkdir(str(PATH_LOGS))
    assert PATH_LOGS.exists(), exit(2)

# Log file path.
PATH_FILE = pathlib.Path(os.path.join(str(PATH_LOGS), FILE))


def get_formatted_utc_now() -> str:
    """
    Returns formatted UTC now string.
    :return:
    """
    return datetime.utcnow().strftime(DT_FORMAT)


def text_append(text: str) -> str:
    """
    Append text with utc dt.
    :param text:
    :return:
    """
    text += "{0}\n".format(get_formatted_utc_now())
    return text


def text_read() -> str:
    """
    Return text from file, else blank text.
    :return:
    """
    if PATH_FILE.is_file():
        return PATH_FILE.read_text(encoding="utf-8")
    else:
        return ''


def text_clean(text: str) -> str:
    """
    Format / clean text.
    :param text:
    :return:
    """
    # Replace double \n's in case this ever happens on windows for some reason.
    if text.__contains__('\n\n'):
        text = text.replace('\n\n', '\n')
    return text


def text_write(text: str):
    """
    Write final text to file.
    :param text:
    :return:
    """
    try:
        PATH_FILE.write_text(text)
        return True
    except Exception as write_err:
        print(write_err)
        return False


def run():
    """
    Runs logging.
    :return:
    """
    log = text_read()
    log = text_append(log)
    log = text_clean(log)
    print('SUCCESS') if text_write(log) else print('FAIL')


if __name__ == '__main__':
    try:
        run()
    except Exception as err:
        print(err)
