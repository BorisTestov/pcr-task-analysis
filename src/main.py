from analyzer.analyzer import Analyzer
from core.settings import app_settings


def main():
    analyzer = Analyzer()
    analyzer.analyze_file(app_settings.input_file)


if __name__ == "__main__":
    main()
