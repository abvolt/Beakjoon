n = int(input())
count = 0
for i in range(1, n+1):
  data = list(str(i))
  if(len(data) == 1 or len(data) == 2):
    count+= 1
  if(len(data) == 3):
    if(int(data[0]) - int(data[1]) == int(data[1]) - int(data[2])):
      count += 1
  else:
    continue
print(count)