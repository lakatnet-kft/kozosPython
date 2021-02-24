import filebe
import harmas
import feladat7
import feladat6

fileName = "eredmenyek.csv"
eredmenyek = []

filebe.filebeolvasas(eredmenyek, fileName)
harmas.hany(eredmenyek)
feladat6.feladat6(eredmenyek)
feladat7.feladat7(eredmenyek)
