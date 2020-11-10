data = []
count = 0
with open('reviews.txt', 'r') as file:
  for f in file:
    data.append(f.strip())
    count += 1
    # if count % 1000 == 0:
    #   print(len(data))
print('Read over, total length is: ', len(data))

sum_len = 0
for d in data:
  sum_len += len(d)
print('Reviews average length is:', sum_len/len(data))

good = []
for d in data:
  if 'good' in d:
    good.append(d)
print('Totally ', len(good), 'have good word')

# List Comprehension
good = [ d for d in data if 'good' in d ]
print(len(good))
