import psutil

while True:
    uso_total = psutil.cpu_percent(interval=1)
    por_nucleo = psutil.cpu_percent(interval=1, percpu=True)

    print(f"CPU Total: {uso_total}%")

    for i, uso in enumerate(por_nucleo):
        print(f"Núcleo {i}: {uso}%")

    print("-" * 30)