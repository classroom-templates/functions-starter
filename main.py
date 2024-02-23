# this file is complete, DO NOT MODIFY IT
# you may modify it while you program, but when you turn in for grading
# it must be returned to EXACTLY this state

# import libraries here
import random as rnd
import functions as fn

def main():

    # never use literals in your code. always make constants and use them instead
    # note these are capitalized to denote they are constants
    MINR = 10
    MAXR = 30
    MINARRAYSIZE = 1
    MAXARRAYSIZE = 10
    
    # this will make a random number from MINARRAYSIZE to MAXARRAYSIZE
    size = rnd.randint(MINARRAYSIZE, MAXARRAYSIZE)

    # this will create and initialize an array of size length
    # with random ints from MIN to MAX (inclusive)
    numbers = fn.make_array(size, MINR, MAXR)
    
    # show the array
    print("Array is size",size)
    print("All the numbers...")
    print(numbers)
    print()
    
    print("The minimum is:", fn.minimum(numbers))
    print("The maximum is:", fn.maximum(numbers))
    print("The total is:", fn.total(numbers))
    print("The average is:", fn.average(numbers))
    print()

    # this will reverse the array
    rnumbers = fn.reverse_array(numbers)

    # show the array
    print("All the numbers...")
    print(numbers)
    print(rnumbers)
    print()

    # the code here will not work until reverse_array() is complete
    # you may want to comment out these lines until you are ready for them
    print("The minimum is:", fn.minimum(rnumbers))
    print("The maximum is:", fn.maximum(rnumbers))
    print("The total is:", fn.total(rnumbers))
    print("The average is:", fn.average(rnumbers))
    print()

# this starts the program
main()
