import filebe
import harmas
import negyes
import otos
import feladat7

fileName = "eredmenyek.csv"
eredmenyek = []

filebe.filebeolvasas(eredmenyek, fileName)
harmas.hany(eredmenyek)
negyes.volte(eredmenyek)
otos.nev(eredmenyek)
feladat7.feladat7(eredmenyek)
