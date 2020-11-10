age = input('age? ')
age = int(age)
if age < 13:
  print('國小')
elif age >= 13 and age < 18:
  print('國中')
else:
  print('多大拉？')
