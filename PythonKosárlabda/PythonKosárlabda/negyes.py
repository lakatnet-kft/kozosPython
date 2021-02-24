def volte(lista):
    volt = 0
    x = 1
    for x in range(len(lista)):
        if lista[x][2]==lista[x][3]:
            volt = 1
    if volt == 1:
        print("4.feladat: Volt döntetlen? Igen")
    else:
        print("4.feladat: Volt döntetlen? Nem")
    