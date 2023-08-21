"""doc

"""

from pathlib import Path
from loguru import logger

print("running okay")

FORMAT_STYLE = "{time:YYYY_MM_DD HH:mm:ss} | {level} | {module}: {function}{line} - {message}"

LOG_DIR = 'logs'
log_filepath = Path(LOG_DIR, "running_logs.log")
Path.mkdir(LOG_DIR, exist_ok= True)

#os.makedirs(log_dir, exist_ok= True)

logger.add(log_filepath,
    format= FORMAT_STYLE,
    level= "INFO",)
