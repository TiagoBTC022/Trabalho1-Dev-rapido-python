f = open("vendas.txt", "r")
array = f.readlines()
print(array)
print(array[5])
for n in range(0, len(array)):
    print(array[n])
f.close
