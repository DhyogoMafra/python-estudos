import psutil
import time

antigo = psutil.net_io_counters()

while True:
    time.sleep(1)
    novo = psutil.net_io_counters()

    download = (novo.bytes_recv - antigo.bytes_recv) / 1024
    upload = (novo.bytes_sent - antigo.bytes_sent) / 1024

    print(f"Download: {download:.2f} KB/s | Upload: {upload:.2f} KB/s")

    antigo = novo