from dotenv import find_dotenv, load_dotenv
from pydantic import Field, field_validator
from pydantic_settings import BaseSettings

load_dotenv(find_dotenv(".env"))


class LogSettings(BaseSettings):
    level: str = "INFO"
    base_filename: str = Field(default="log", min_length=1)
    directory: str = Field(default="logs", min_length=1)
    rotation_value: int = Field(default=5, ge=1)

    @field_validator("level")
    @classmethod
    def check_logging_level(cls, value):
        valid_levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
        value = value.upper()
        if value not in valid_levels:
            raise ValueError(
                f"Invalid logging level: {value}. Valid levels are: {valid_levels}"
            )
        return value

    class Config:
        env_prefix = "LOG_"


class AppSettings(BaseSettings):
    input_file: str
    output_file: str = Field(default="statistics.json", min_length=1)
    output_chart: str = Field(default="chart.png", min_length=1)
    show_chart: bool = Field(default=True)


log_settings = LogSettings()
app_settings = AppSettings()
