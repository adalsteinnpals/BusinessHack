import pandas as pd

regnskab = pd.read_csv('Regnskab.csv', error_bad_lines=False)

print(regnskab.head())



