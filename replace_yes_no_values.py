import pandas as pd

# Lê o arquivo CSV original com valores 'Yes' e 'No'
df = pd.read_csv('personality_datasert.csv')

# Substitui 'Yes' por True e 'No' por False
df = df.replace({'Yes': True, 'No': False})

# Salva novo arquivo CSV com as alterações
df.to_csv('personality_datasert_converted.csv', index=False)
