from math import *
import math


#Prime number Sieve O(n^2)
#Sieve of Erathothesis
#Prime number array creator
def primeGenerator(n):
    #creates empty array
    array = []

    #creates an array of boolean true upto n
    for x in range(1, n + 1):
        array.append(True)

    #finds goes from 2 to sqrt(n)
    for i in range(2, int(sqrt(n))):
        if array[i] == True:

            #inner loop finds squares from range 2 - sqrt(n)
            #cancels them out as non-prime
            for j in range((i*i) , n, i):
                array[j] = False

    #uses list comprehension to get numbers from the array of boolean
    array = [i for i, x in enumerate(array) if x == True]
    array.remove(0)
    array.remove(1)

    #returns array of primes upto n
    return array

#Prime checker
def isPrime(number):

    #does a loop from 2 to number and checks for mod
    for x in range(2, number//2):
        remainder = number % x

        #returns False as soon as divisor is found
        if remainder == 0:
            return False

    #returns True if there is no divisor
    return True

#Prime Factorization
def findPrimes(n):
    listPrimes = []
    while (n%2 == 0):
        listPrimes.append(2)
        n = n/ 2

    for x in range(3, int(sqrt(n))+1, 2):
        while (n%x == 0):
            listPrimes.append(int(x))
            n = n / x

    if (n > 2):
        listPrimes.append(int(n))


    return listPrimes