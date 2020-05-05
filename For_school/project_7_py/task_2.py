n = input('Enter n : ')[::-1]
indt = True
for i in range(len(n) - 1):
    if n[i] <= n[i+1]:
        pass
    else:
        indt = False
        break
print(indt)