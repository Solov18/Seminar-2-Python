# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 4 

b = int(input('Введите число A: '))
a = int(b)
caunt = 0
fib1 = 0
fib2 = 1
while fib2 < a   :
    fibsum = fib1 + fib2
    fib1 = fib2
    fib2 = fibsum
    caunt +=1
    print( fib2, end= ' , ')
    
if fib2 == a :
    print(f'\n {caunt} по счету является числом Фибоччи'   )   
else:
    print(' -  это число не из списка Фибоначчи')    