data = []
count = 0
with open('test.txt', 'r') as file:
  for f in file:
    data.append(f.strip())
    count += 1
    if count % 1000 == 0:
      print(len(data))

print(data, len(data))
