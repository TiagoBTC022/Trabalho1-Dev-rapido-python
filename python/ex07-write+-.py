f = open("creat.txt", "w+")

text = ["jacare", "salgueiro", "cdd", "madureira"]

for l in text:
    f.write(l)
    f.write("\n")
f.close()

f = open("creat.txt", "r")
for l in f:
    print(l)
f.close()