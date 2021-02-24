def hany(lista):
    x = 1
    hazai = 0
    idegen = 0
    for x in range(len(lista)):
        if lista[x][0]=="Real Madrid":
            hazai += 1
        if lista[x][1]=="Real Madrid":
            idegen += 1
    print("3.feladat: Real Madrid: Hazai: "+str(hazai)+", Idegen: "+str(idegen))