


for i in range(2):
    for j in range(10):
        print(j, end='\t')

for row in range(10):
    for col in range(row+1):
        print('*', end=' ')
    print('')


# \O/
# \O/\O/
# \O/\O/\O/
# \O/\O/
# \O/
n=5

for row in range(int((n+1)/2)):
    for col in range(row+1):
        print('\\o/', end=' ')
    print('')

for row in range(int((n-1)/2), 0, -1):
    for col in range(row):
        print('\\o/', end=' ')
    print('')

