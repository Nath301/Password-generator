import random
lst = []
def random_letter():

  while len(lst) < 20:
    letter = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890&_-@$./')
    lst.append(letter)
    password = "".join(lst)
  return password

print('Your new password is : ' + random_letter())