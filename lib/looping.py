#!/usr/bin/env python3
import ipdb

def happy_new_year():
    counter = 10
    while counter > 0:
        print(counter)
        counter -= 1
    print ("Happy New Year!")
    # ipdb.set_trace()

def square_integers(int_list):

##traditional way:
    # square_int_list = []
    # for num in int_list:
    #     # print(num*num)
    #     square_int_list.append(num**2)
    # return(square_int_list)

##using list comprehension:
    return [(num**2) for num in int_list]

def fizzbuzz():
    for num in range(1, 100 + 1):
        if num % 3 == 0 and num % 5==0:  ##can also do: if num % 15 == 0
            print ("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)



print(happy_new_year())
print(square_integers([1,2,3,4]))
fizzbuzz()