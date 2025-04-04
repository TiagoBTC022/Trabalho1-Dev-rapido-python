f = open("vendas-utf-8.txt", "r", encoding="utf-8")

print("Nome do arquivo: ", f.name)
print("Modo do arquivo: ", f.mode)
print("O arquivo esta fechado? : ", f.closed)
f.close()
print("O arquivo esta fechado? : ", f.closed)