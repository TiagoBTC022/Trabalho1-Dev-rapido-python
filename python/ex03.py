f = open("readline.txt", "r")
while True:
    linha = f.readline()    
    if not linha:
        break
    print(linha)
f.close()