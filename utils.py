from datetime import datetime
from config import DT_FORMAT


class Utils:
    @staticmethod
    def get_formatted_utc_now() -> str:
        """
        Returns formatted UTC now string.
        :return:
        """
        return datetime.utcnow().strftime(DT_FORMAT)
