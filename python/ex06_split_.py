f = open("vendas-utf-8.txt", "r", encoding="utf-8")
for l in f:
    print(l.split())
f.close()