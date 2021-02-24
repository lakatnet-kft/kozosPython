import filebe
import harmas
import negyes
fileName = "eredmenyek.csv"
eredmenyek = []

filebe.filebeolvasas(eredmenyek, fileName)
harmas.hany(eredmenyek)
negyes.volte(eredmenyek)