def feladat7(lista):
    helyszinek = []
    for i in range(1, len(lista)):
        db = 0
        helyszin = lista[i][4]
        ideiglenes = []
        letezik = 0
        for j in range(1, len(lista)):
            if lista[j][4] == helyszin:
                db = db + 1
        for j in range(0, len(helyszinek)):
            if helyszin == helyszinek[j][0]:
                letezik = 1
        if letezik == 0:
            ideiglenes.append(helyszin)
            ideiglenes.append(db)
            helyszinek.append(ideiglenes)
    for i in range(0, len(helyszinek)):
        if helyszinek[i][1] > 20:
            print(str(helyszinek[i][0]) +":" + str(helyszinek[i][1]))
            