f = open("vendas.txt", "r")
for l in f:
    print(l)
f.close()
print("--"*30)
f = open("readline.txt", "r")
for l in f:
    print(l)
f.close()