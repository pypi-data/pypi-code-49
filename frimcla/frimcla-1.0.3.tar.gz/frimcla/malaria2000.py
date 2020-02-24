
import shutil
file = open("/home/magarcd/Escritorio/malaria2000.txt", "r")

for line in file.readlines():
    lisplit=line.split("/")
    line=line[:-1]
    if lisplit[-2] == "Parasitized":
        shutil.copy(line, "/home/magarcd/Escritorio/dataset/malaria2000/Parasitized")
    else:
        shutil.copy(line, "/home/magarcd/Escritorio/dataset/malaria2000/Uninfected")
