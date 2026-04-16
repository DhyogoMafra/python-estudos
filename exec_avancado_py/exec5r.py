import psutil

limite = 10  # %

for p in psutil.disk_partitions():
    uso = psutil.disk_usage(p.mountpoint)

    if uso.percent > (100 - limite):
        print(f"⚠️ Pouco espaço em {p.mountpoint}")