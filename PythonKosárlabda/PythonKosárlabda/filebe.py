def filebeolvasas(lista, filenev):
    f = open(filenev)
    for x in f:
        lista.append(x.strip().split(';'))
    f.close()