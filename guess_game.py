number = 9
guess_limit = 3
guess_count = 0
while guess_count < guess_limit:
     guess = int(input('Enter:'))
     if guess == number:
         print('You won!')
         break
     guess_count = guess_count + 1
else:
    print('Sorry, you failed!')