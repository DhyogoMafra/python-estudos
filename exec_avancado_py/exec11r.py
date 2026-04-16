import psutil
import time
import os

antigo = psutil.net_io_counters()

while True:
    os.system("cls")  # Windows

    # RAM
    mem = psutil.virtual_memory()

    # CPU
    cpu = psutil.cpu_percent()

    # Disco (C:)
    disco = psutil.disk_usage("C:\\")

    # Rede
    time.sleep(1)
    novo = psutil.net_io_counters()

    down = (novo.bytes_recv - antigo.bytes_recv) / 1024
    up = (novo.bytes_sent - antigo.bytes_sent) / 1024

    antigo = novo

    print("=== MONITOR ===\n")
    print(f"RAM: {mem.percent}% ({mem.used / (1024**2):.2f} MB)")
    print(f"CPU: {cpu}%")
    print(f"Disco livre: {disco.free / (1024**3):.2f} GB")
    print(f"Download: {down:.2f} KB/s | Upload: {up:.2f} KB/s")

    time.sleep(1)