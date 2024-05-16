from matplotlib import pyplot as plt

from core.logger import get_logger
from core.settings import app_settings
from models.statistics import Statistics

logger = get_logger(__name__)


class Plotter:
    @staticmethod
    def plot(statistics: Statistics) -> None:
        data = statistics.dict()

        sprints = [stat["sprint"] for stat in data["sprints_statistics"]]
        total_students = [
            stat["total_students"] for stat in data["sprints_statistics"]
        ]

        fig, ax = plt.subplots(figsize=(10, 6))
        bars = ax.bar(sprints, total_students, color="skyblue")

        for bar in bars:
            height = bar.get_height()
            ax.annotate(
                height,
                xy=(bar.get_x() + bar.get_width() / 2, height / 2),
                ha="center",
                va="center",
                fontsize=15,
                weight="bold",
            )

        ax.set_title("Total Students per sprint", fontsize=20)
        ax.set_xticks(sprints)

        ax.yaxis.label.set_size(20)
        ax.xaxis.label.set_size(20)
        ax.tick_params(axis="both", which="major", labelsize=12)

        text = f"""
        Total Tasks: {data["total_tasks"]}
        Total Students: {data["total_students"]}
        Start Date: {data["first_task_date"]}
        End Date: {data["last_task_date"]}
        Total days: {(data["last_task_date"] - data["first_task_date"]).days}
        """

        plt.text(
            0.3,
            -0.3,
            text,
            ha="left",
            va="center",
            transform=ax.transAxes,
            fontsize=15,
        )

        plt.tight_layout()

        logger.info(f"Saving chart to file {app_settings.output_chart}")
        plt.savefig(app_settings.output_chart)

        if app_settings.show_chart:
            plt.show()
