f = open("jacare.txt", "w")
f.write("Eu vo largar minha casa e traficar no jacare\n")
f.close()

p = open("jacare.txt", "r")
print(p.read())
p.close()
