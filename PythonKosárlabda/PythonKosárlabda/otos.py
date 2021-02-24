def nev(lista):
    x = 1
    nev = ""
    for x in range(len(lista)):
        if "Barcelona" in lista[x][0]:
            nev = lista[x][0]
    print("5.feladat: barcelonai csapat neve: "+nev)