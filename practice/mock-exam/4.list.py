L = [1.5, 'Python', False]
T = (1.2, 'Java', 'True')

for i in range(len(L)):
    if L[i]:
        L[i] = L[i] + T[i]
    else:
        T[i] = L[i] + T[i]
print(i)