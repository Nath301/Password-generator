import random
lst = []
def random_letter():

  while len(lst) < 12:
    letter = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890&_-@$./')
    lst.append(letter)
    password = "".join(lst)
  return password

print('Your new password is : {}'.format(random_letter()))