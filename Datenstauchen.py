
import os
#import csv
import pandas as pd
#pd.set_option('display.max_columns', 1000)

df = pd.read_csv("Umsaetze.csv", sep=";")

df.rename(columns={"Name Zahlungsbeteiligter": "Zahlungsbeteiligter", "Saldo nach Buchung": "Saldo"}, inplace = True)
#Dropping sensitive and non-useful data
df.drop("IBAN Auftragskonto", axis = 1, inplace = True)
df.drop("Bezeichnung Auftragskonto", axis = 1, inplace = True)
df.drop("BIC Auftragskonto", axis = 1, inplace = True)
df.drop("IBAN Zahlungsbeteiligter", axis = 1, inplace = True)
df.drop("Bankname Auftragskonto", axis = 1, inplace = True)
df.drop("Valutadatum", axis = 1, inplace = True)
df.drop("BIC (SWIFT-Code) Zahlungsbeteiligter", axis = 1, inplace = True)
df.drop("Bemerkung", axis = 1, inplace = True)
df.drop("Kategorie", axis = 1, inplace = True)
df.drop("Steuerrelevant", axis = 1, inplace = True)
df.drop("Glaeubiger ID", axis = 1, inplace = True)
df.drop("Mandatsreferenz", axis = 1, inplace = True)
df = df[df.Zahlungsbeteiligter.notnull()]

#Output to .csv
df.to_csv("Daten_gestaucht.csv", index= False, sep= ";", encoding="utf-8-sig")
