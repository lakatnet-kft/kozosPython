import filebe
import harmas
import negyes
import otos
import feladat6
import feladat7

fileName = "eredmenyek.csv"
eredmenyek = []

filebe.filebeolvasas(eredmenyek, fileName)
harmas.hany(eredmenyek)
negyes.volte(eredmenyek)
otos.nev(eredmenyek)
feladat6.feladat6(eredmenyek)
feladat7.feladat7(eredmenyek)