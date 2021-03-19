def my_range(first=0,last=10, step=1):
    number=first
    while number < last:
        yield number
        number += step
ranger = my_range(40,99)   
for x in ranger:
    print(x)




