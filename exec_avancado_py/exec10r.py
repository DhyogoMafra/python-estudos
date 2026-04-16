import psutil

particoes = psutil.disk_partitions()

for i, p in enumerate(particoes):
    print(f"{i} - {p.mountpoint}")

op = int(input("Escolha: "))
p = particoes[op]

uso = psutil.disk_usage(p.mountpoint)

print(f"\nDetalhes de {p.mountpoint}")
print(f"Total: {uso.total}")
print(f"Usado: {uso.used}")
print(f"Livre: {uso.free}")