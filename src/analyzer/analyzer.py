from collections import defaultdict

import orjson
import pandas as pd

from analyzer.parser import Parser
from analyzer.plotter import Plotter
from core.constants import MAX_SPRINT_NUMBER, MIN_SPRINT_NUMBER
from core.logger import get_logger
from core.settings import app_settings
from models.statistics import SprintStatistics, Statistics
from models.task import Task

logger = get_logger(__name__)


class Analyzer:
    def analyze_file(self, file_path: str) -> None:
        tasks = self.get_completed_tasks(file_path)
        logger.info(f"Found {len(tasks)} completed tasks")
        statistics = self.get_statistics(tasks)
        self.save_statistics(statistics)
        Plotter.plot(statistics)

    def get_completed_tasks(self, file_path: str) -> list[Task]:
        logger.info(f"Analyzing file {file_path}")
        df = pd.read_csv(file_path, usecols=["Задача", "Статус", "Создано"])
        df = df[df["Статус"] == "Решен"]
        tasks = []
        for task, date in zip(df["Задача"].tolist(), df["Создано"].tolist()):
            sprint, name = Parser.get_task_from_string(task)
            date = Parser.get_date_from_string(date)
            tasks.append(Task(sprint=sprint, username=name, date=date))
        return tasks

    def get_statistics(self, tasks: list[Task]) -> Statistics:
        unique_usernames = set()
        unique_usernames_by_sprints = defaultdict(set)
        min_task_date = None
        max_task_date = None

        for task in tasks:
            unique_usernames.add(task.username)
            if task.sprint in range(MIN_SPRINT_NUMBER, MAX_SPRINT_NUMBER + 1):
                unique_usernames_by_sprints[task.sprint].add(task.username)
            if min_task_date is None or task.date < min_task_date:
                min_task_date = task.date
            if max_task_date is None or task.date > max_task_date:
                max_task_date = task.date

        logger.info(
            f"Found {len(unique_usernames)} unique usernames among all sprints"
        )
        for sprint, tasks_list in sorted(
            unique_usernames_by_sprints.items(), key=lambda x: x[0]
        ):
            logger.info(
                f"Found {len(tasks_list)} unique usernames for sprint {sprint}"
            )

        return Statistics(
            total_students=len(unique_usernames),
            total_tasks=len(tasks),
            sprints_statistics=[
                SprintStatistics(
                    sprint=sprint,
                    total_students=len(unique_usernames_by_sprints[sprint]),
                )
                for sprint in range(MIN_SPRINT_NUMBER, MAX_SPRINT_NUMBER + 1)
            ],
            first_task_date=min_task_date,
            last_task_date=max_task_date,
        )

    def save_statistics(self, statistics: Statistics) -> None:
        logger.info(f"Saving statistics to file {app_settings.output_file}")
        with open(app_settings.output_file, "wb") as f:
            f.write(
                orjson.dumps(statistics.dict(), option=orjson.OPT_INDENT_2)
            )
