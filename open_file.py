data = []
with open('test.txt', 'r') as file:
  for f in file:
    data.append(f.strip())

print(data, len(data))
