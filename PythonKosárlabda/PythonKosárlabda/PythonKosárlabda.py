import filebe
import harmas
import feladat7

fileName = "eredmenyek.csv"
eredmenyek = []

filebe.filebeolvasas(eredmenyek, fileName)
harmas.hany(eredmenyek)
feladat7.feladat7(eredmenyek)