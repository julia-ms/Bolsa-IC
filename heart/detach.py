import pandas as pd

data = pd.read_csv('heart/heart.csv')

# sex (1 = male; 0 = female)
male = data[data['sex'] == 1]
fem = data[data['sex'] == 0]

# Excluir a coluna 'sex'
male = male.drop(columns=['sex'])
fem = fem.drop(columns=['sex'])
data = data.drop(columns=['sex'])

male.to_csv('heart/male.csv', index=False)
fem.to_csv('heart/female.csv', index=False)
data.to_csv('heart/heart.csv', index=False)