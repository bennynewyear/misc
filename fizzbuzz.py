"""
    Fizzbuzz test -- print numbers 1 to 100; for multiples of 3, print 'fizz';
                     for multiples of 5, print 'buzz'; for multiples of 3 and 5,
                     print 'fizzbuzz'
    file: fizzbuzz.py
    author: Benny Tan
    created: July 30, 2017
"""

def fizzbuzz():
    i = 1
    while(i <= 100):
        if((i % 3 == 0) and (i % 5 == 0)):
            print("fizzbuzz")
        elif(i % 3 == 0):
            print("fizz")
        elif(i % 5 == 0):
            print("buzz")
        else:
            print(i)
        i = i + 1

fizzbuzz()      
    
