for fizzbuzz in range(100):
    if fizzbuzz % 3==0 and fizzbuzz % 5 ==0:
        print('Fizzbuzz')
        continue
    elif fizzbuzz % 3 == 0:
        print('Fizz')
        continue
    elif fizzbuzz % 5 == 0:
        print('Buzz')
        continue
    elif fizzbuzz % 5 != 0 and fizzbuzz % 3 != 0:
        print('Number')
        continue
