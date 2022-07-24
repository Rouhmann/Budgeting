
import os
#import csv
import pandas as pd
#pd.set_option('display.max_columns', 1000)

df = pd.read_csv("Umsaetze.csv", sep=";")

df.rename(columns={"Name Zahlungsbeteiligter": "Zahlungsbeteiligter", "Saldo nach Buchung": "Saldo"}, inplace = True)
#Dropping sensitive and non-useful data

col_drop = ["IBAN Auftragskonto",  "Bezeichnung Auftragskonto", "BIC Auftragskonto", "IBAN Zahlungsbeteiligter", "Bankname Auftragskonto", "Valutadatum",
"BIC (SWIFT-Code) Zahlungsbeteiligter", "Bemerkung", "Kategorie","Steuerrelevant", "Glaeubiger ID", "Mandatsreferenz"]
for col in col_drop:
    df.drop(col, axis = 1, inplace = True)

df = df[df.Zahlungsbeteiligter.notnull()]

#Output to .csv
df.to_csv("Daten_gestaucht.csv", index= False, sep= ";", encoding="utf-8-sig")
