data = []
for i in range(30):
  data.append(i + 1)
for k in range(28):
  n = int(input())
  data.remove(n)
print(data[0])
print(data[1])