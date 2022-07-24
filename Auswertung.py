
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Daten_gestaucht.csv", sep=";")

#df2 = df.groupby(['Zahlungsbeteiligter'])['Zahlungsbeteiligter'].count()
#print(df2)

df['Zahlungsbeteiligter'] = df['Zahlungsbeteiligter'].astype('category')

others = df['Zahlungsbeteiligter'].value_counts().index[10:]
label = 'Andere'

df['Zahlungsbeteiligter'] = df['Zahlungsbeteiligter'].cat.add_categories([label])
df['Zahlungsbeteiligter'] = df['Zahlungsbeteiligter'].replace(others, label)

df2 = df.groupby(['Zahlungsbeteiligter'])['Zahlungsbeteiligter'].count()
print(df2)

df2.groupby(['Zahlungsbeteiligter']).sum().plot(
    kind='pie', y='Verteilung', autopct='%1.0f%%', startangle=200)
plt.show()
