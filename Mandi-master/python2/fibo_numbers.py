from Yu import fib2

number = input('Choose a number:')

print(fib2(int(number)))

if int(number) > 200:
    print('That is a big number')
elif int(number) < 20:
    print('That is a small number')
else:
    print('Good number')
    print('Fibonacci')
    
