import psutil

particoes = psutil.disk_partitions()

for p in particoes:
    uso = psutil.disk_usage(p.mountpoint)

    print(f"\nPartição: {p.mountpoint}")
    print(f"Total: {uso.total / (1024**3):.2f} GB")
    print(f"Usado: {uso.used / (1024**3):.2f} GB")
    print(f"Livre: {uso.free / (1024**3):.2f} GB")
    print(f"Uso: {uso.percent}%")