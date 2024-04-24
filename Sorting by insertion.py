a = [-3, 11, 4, -7, 8, 5]
N = len(a)

for i in range(1, N):
  for j in range(i, 0, -1):
    if a[j] < a[j - 1]:
      a[j], a[j - 1] = a[j - 1], a[j]
    else:
      break

print(a)