import os

arq = os.scandir()

for obj in arq:
    print(obj.is_dir())

