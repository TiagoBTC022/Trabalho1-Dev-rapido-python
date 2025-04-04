#fazendo de um jeito que fecha sozinho
with open("jacaret.txt", "w") as f:
    f.write("Eu vo largar minha casa e traficar no jacare\n")
    f.write("EU vou comer seu COOL no uno\n")

#fazendo tendo que abrir e fechar manialmente
p = open("jacaret.txt", "r")
print(p.read())
p.close()

with open("jacaret.txt", "a") as g:
    g.write("Eu sou pobre pobre pobre pobre de marre\n")

with open("jacaret.txt", "r") as t:
    print(t.read())
