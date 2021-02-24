def filebeolvasas(lista, filenev):
    f = open(filenev, encoding=UTF-8)
    for x in f:
        sor = x.split().strip(';')
        lista.append(sor[0],sor[1],sor[2],sor[3],sor[4],sor[5])
    f.close()