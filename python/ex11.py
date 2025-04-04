import os

arq = os.scandir()

print("--"*30)
print(arq)

print("--"*30)

for obj in arq:
    print(arq)
print("--"*30)

with os.scandir() as arq:
    for entry in arq:
        print(entry.name)  # Exibe o nome dos arquivos e subdiretórios
