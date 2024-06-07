import pandas as pd

data = pd.read_excel('intersectionalBias.xlsx')

# Race
asian = data[data['Race'] == 'Asian']
hispanic = data[data['Race'] == 'Hispanic']
black = data[data['Race'] == 'Black']
white = data[data['Race'] == 'White']

asian.to_excel('asian.xlsx', index=False)
hispanic.to_excel('hispanic.xlsx', index=False)
black.to_excel('black.xlsx', index=False)
white.to_excel('white.xlsx', index=False)

# Sex
male = data[data['Sex'] == 'Male']
female = data[data['Sex'] == 'Female']

male.to_excel('male.xlsx', index=False)
female.to_excel('female.xlsx', index=False)

# Housing
stable = data[data['Housing'] == 'Stable']
unstable = data[data['Housing'] == 'Unstable']

stable.to_excel('stable.xlsx', index=False)
unstable.to_excel('unstable.xlsx', index=False)

# Race - Sex
asianF = asian[asian['Sex'] == 'Female']
hispanicF = hispanic[hispanic['Sex'] == 'Female']
blackF = black[black['Sex'] == 'Female']
whiteF = white[white['Sex'] == 'Female']

asianM = asian[asian['Sex'] == 'Male']
hispanicM = hispanic[hispanic['Sex'] == 'Male']
blackM = black[black['Sex'] == 'Male']
whiteM = white[white['Sex'] == 'Male']

asianF.to_excel('asianFem.xlsx', index=False)
hispanicF.to_excel('hispanicFem.xlsx', index=False)
blackF.to_excel('blackFem.xlsx', index=False)
whiteF.to_excel('whiteFem.xlsx', index=False)

asianM.to_excel('asianMale.xlsx', index=False)
hispanicM.to_excel('hispanicMale.xlsx', index=False)
blackM.to_excel('blackMale.xlsx', index=False)
whiteM.to_excel('whiteMale.xlsx', index=False)

# Race - Housing
asianS = asian[asian['Housing'] == 'Stable']
hispanicS = hispanic[hispanic['Housing'] == 'Stable']
blackS = black[black['Housing'] == 'Stable']
whiteS = white[white['Housing'] == 'Stable']

asianU = asian[asian['Housing'] == 'Unstable']
hispanicU = hispanic[hispanic['Housing'] == 'Unstable']
blackU = black[black['Housing'] == 'Unstable']
whiteU = white[white['Housing'] == 'Unstable']

asianS.to_excel('asianStable.xlsx', index=False)
hispanicS.to_excel('hispanicStable.xlsx', index=False)
blackS.to_excel('blackStable.xlsx', index=False)
whiteS.to_excel('whiteStable.xlsx', index=False)

asianU.to_excel('asianUnstable.xlsx', index=False)
hispanicU.to_excel('hispanicUnstable.xlsx', index=False)
blackU.to_excel('blackUnstable.xlsx', index=False)
whiteU.to_excel('whiteUnstable.xlsx', index=False)

# Sex - Housing
maleS = male[male['Housing'] == 'Stable']
femaleS = female[female['Housing'] == 'Stable']

maleU = male[male['Housing'] == 'Unstable']
femaleU = female[female['Housing'] == 'Unstable']

maleS.to_excel('maleStable.xlsx', index=False)
femaleS.to_excel('femaleStable.xlsx', index=False)

maleU.to_excel('maleUnstable.xlsx', index=False)
femaleU.to_excel('femaleUnstable.xlsx', index=False)

# Race - Sex - Housing

asianFS = asianF[asianF['Housing'] == 'Stable']
hispanicFS = hispanicF[hispanicF['Housing'] == 'Stable']
blackFS = blackF[blackF['Housing'] == 'Stable']
whiteFS = whiteF[whiteF['Housing'] == 'Stable']
asianMS = asianM[asianM['Housing'] == 'Stable']
hispanicMS = hispanicM[hispanicM['Housing'] == 'Stable']
blackMS = blackM[blackM['Housing'] == 'Stable']
whiteMS = whiteM[whiteM['Housing'] == 'Stable']

asianFS.to_excel('asianFemSta.xlsx', index=False)
hispanicFS.to_excel('hispanicFemSta.xlsx', index=False)
blackFS.to_excel('blackFemSta.xlsx', index=False)
whiteFS.to_excel('whiteFemSta.xlsx', index=False)
asianMS.to_excel('asianMaleSta.xlsx', index=False)
hispanicMS.to_excel('hispanicMaleSta.xlsx', index=False)
blackMS.to_excel('blackMaleSta.xlsx', index=False)
whiteMS.to_excel('whiteMaleSta.xlsx', index=False)

asianFU = asianF[asianF['Housing'] == 'Unstable']
hispanicFU = hispanicF[hispanicF['Housing'] == 'Unstable']
blackFU = blackF[blackF['Housing'] == 'Unstable']
whiteFU = whiteF[whiteF['Housing'] == 'Unstable']
asianMU = asianM[asianM['Housing'] == 'Unstable']
hispanicMU = hispanicM[hispanicM['Housing'] == 'Unstable']
blackMU = blackM[blackM['Housing'] == 'Unstable']
whiteMU = whiteM[whiteM['Housing'] == 'Unstable']

asianFU.to_excel('asianFemUnst.xlsx', index=False)
hispanicFU.to_excel('hispanicFemUnst.xlsx', index=False)
blackFU.to_excel('blackFemUnst.xlsx', index=False)
whiteFU.to_excel('whiteFemUnst.xlsx', index=False)
asianMU.to_excel('asianMaleUnst.xlsx', index=False)
hispanicMU.to_excel('hispanicMaleUnst.xlsx', index=False)
blackMU.to_excel('blackMaleUnst.xlsx', index=False)
whiteMU.to_excel('whiteMaleUnst.xlsx', index=False)


