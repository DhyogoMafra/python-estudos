import psutil
import time
from datetime import datetime

while True:
    uso = psutil.cpu_percent(interval=1)
    agora = datetime.now()

    with open("cpu_log.txt", "a") as f:
        f.write(f"{agora} - CPU: {uso}%\n")

    time.sleep(5)