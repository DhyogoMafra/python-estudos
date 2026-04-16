import psutil
import time

limite = float(input("Digite o limite (%): "))

while True:
    mem = psutil.virtual_memory()

    print(f"Uso: {mem.percent}%")

    if mem.percent > limite:
        print("⚠️ ALERTA: Uso de RAM alto!")

    time.sleep(2)