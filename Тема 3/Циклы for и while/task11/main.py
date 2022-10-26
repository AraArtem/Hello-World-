num = 123
count = 0

# TODO посчитать количество действий над числом согласно условию
while num != 1:
    if num % 2 == 1:
        num *= 3
        num += 1
    num //= 2
    count += 1

print(count)
