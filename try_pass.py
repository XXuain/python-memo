rightPass = 'a123456'
count = 3
while True:
  print(count, 'more chance')
  userPass = input('Ur Pass: ')
  count -= 1
  if count >= 0 and userPass == rightPass:
    print('Login success!')
    break;
  elif count == 0:
    print('ur cant try anymore!!')
    break;
