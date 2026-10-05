# Отчет по продажам

import pandas as pd
df = pd.read_csv('data.csv')
df.groupby('date').sum()
