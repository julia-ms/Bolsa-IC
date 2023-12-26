txt = 'txt.txt'
results = 'results.csv'

with open(txt, 'r') as file:
    lines = file.readlines()

values = []

for line in lines:
    #if line.strip() and line.lower().strip().endswith('ority'):
    if line.strip() and not line.lower().strip().endswith('ority'):
        values.extend([value.strip() for value in line.split()])

data = ';'.join(values)

with open(results, 'a') as file:
    file.write('\n')
    file.write(data)

print("ok")
