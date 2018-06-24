from utils import Utils


class Text:
    def __init__(self, file_path):
        self.file_path = file_path
        self.text = ''

    def append(self):
        """
        Append text with utc dt.
        :return:
        """
        self.text += "{0}\n".format(Utils.get_formatted_utc_now())

    def read(self):
        """
        Return text from file, else blank text.
        :return:
        """
        if self.file_path.is_file():
            self.text = self.file_path.read_text(encoding="utf-8")

    def clean(self):
        """
        Format / clean text.
        :return:
        """
        # Replace double \n's in case this ever happens on windows for some reason.
        if self.text.__contains__('\n\n'):
            self.text = self.text.replace('\n\n', '\n')

    def write(self):
        """
        Write final text to file.
        :return:
        """
        try:
            self.file_path.write_text(self.text)
            return True
        except Exception as write_err:
            print(write_err)
            return False

    def execute(self):
        """
        Run.
        :return:
        """
        self.read()
        self.append()
        self.clean()
        return self.write()
