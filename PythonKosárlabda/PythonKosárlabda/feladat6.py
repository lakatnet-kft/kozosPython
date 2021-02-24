def feladat6(lista):
    print("6. feladat:")
    datum = "2004-11-21"
    for i in range(1, len(lista)):
        if lista[i][5] == datum:
            print("\t"+lista[i][0] + " - " + lista[i][1] + " (" + lista[i][2] + ":" + lista[i][3] + ")")