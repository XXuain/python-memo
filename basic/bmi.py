height = input('ur height: ')
weight = input('ur weight: ')
height = int(height) / 100
weight = int(weight)

bmi = weight / (height * height)
print(bmi)

if bmi < 18.5:
  print('太輕')
elif bmi >= 18.5 and bmi < 20:
  print('正常')
else:
  print('有點胖')
