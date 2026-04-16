import psutil
import time

while True:
    mem = psutil.virtual_memory()

    total = mem.total / (1024**2)
    usado = mem.used / (1024**2)
    livre = mem.available / (1024**2)

    print(f"Total: {total:.2f} MB")
    print(f"Usado: {usado:.2f} MB")
    print(f"Livre: {livre:.2f} MB ({mem.percent}%)")
    print("-" * 30)

    time.sleep(2)