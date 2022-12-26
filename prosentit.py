import re

file = open('veroprosentit.txt', 'r')
lines = file.readlines()

incomes = []
percentages = []

def sanitize(s):
    s = s.replace(",", ".")
    x = float(re.sub(r'[^0-9.]', '', s))
    return x

i = 1
for line in lines:
    if i % 5 == 1:
        x = int(sanitize(line))
        incomes.append(x)
    elif i % 5 == 3:
        x = sanitize(line)
        x = round(x - 8.7, 2)
        percentages.append(x)

    i += 1

output = "veroprosentit = ["
for income, percent in zip(incomes, percentages):
    output += '{' + str(income) + ': ' + str(percent) + '}, '

output += "]"
print(output)

#print(incomes)
#print(percentages)