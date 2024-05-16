import re
from datetime import date, datetime

from pydantic import ValidationError

from core.logger import get_logger

logger = get_logger(__name__)


class Parser:
    @staticmethod
    def get_task_from_string(input_string: str) -> tuple[int, str]:
        pattern = r"\[(\d)\]\s+(.*?)\s+\((.*?)\)"
        match = re.match(pattern, input_string)

        try:
            if match:
                number = match.group(1)
                name = match.group(2)
                return int(number), name
            else:
                raise ValueError(
                    f"The input string '{input_string}' does not match the expected format."
                )
        except ValidationError as e:
            logger.error(
                f"Validation error for input string '{input_string}': {e}"
            )
            raise
        except Exception as e:
            logger.error(
                f"Unexpected error for input string '{input_string}': {e}"
            )
            raise

    @staticmethod
    def get_date_from_string(input_string: str) -> date:
        months = {
            "января": "01",
            "февраля": "02",
            "марта": "03",
            "апреля": "04",
            "мая": "05",
            "июня": "06",
            "июля": "07",
            "августа": "08",
            "сентября": "09",
            "октября": "10",
            "ноября": "11",
            "декабря": "12",
        }

        for month in months:
            if month in input_string:
                input_string = input_string.replace(month, months[month])
                break
        else:
            raise ValueError(
                f"The input string '{input_string}' does not match the expected format."
            )

        date_time_obj = datetime.strptime(input_string, "%d %m %Y в %H:%M")

        date_obj = date_time_obj.date()

        return date_obj
