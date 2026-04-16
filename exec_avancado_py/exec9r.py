import psutil
import platform

print("Processador:", platform.processor())
print("Núcleos físicos:", psutil.cpu_count(logical=False))
print("Núcleos lógicos:", psutil.cpu_count(logical=True))

freq = psutil.cpu_freq()
print(f"Frequência: {freq.current:.2f} MHz")

print("Número de série: Não disponível (limitação do sistema)")