# How to start

- Copy `.env.example` to `.env`
- Install requirements. `pip install -r requirements.txt`
- Setup env variables.
- Run `python src/main.py`

# Env variables

| Name               | Description                                                         | Is optional | Default         |
|--------------------|---------------------------------------------------------------------|-------------|-----------------|
| INPUT_FILE         | Path to .csv file with data for analysis                            | False       | -               |
| OUTPUT_FILE        | Path to .json file with saved statistics                            | True        | statistics.json |
| OUTPUT_CHART       | Path to .png file with saved chart                                  | True        | chart.png       |
| SHOW_CHART         | Show chart and save file on run if True, else only save to file     | True        | True            |
| LOG_LEVEL          | Log level. One of ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] | True        | INFO            |
| LOG_BASE_FILENAME  | Base filename (prefix) for log files                                | True        | log             |
| LOG_DIRECTORY      | Directory to store logs. Auto created                               | True        | logs            |
| LOG_ROTATION_VALUE | How much log files to store. One log file == one app run            | True        | 5               |
