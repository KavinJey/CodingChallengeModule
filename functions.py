from math import *
import math

#Collection of Functions that can prove useful in competetive coding
#ADD ON TO THE ALGORITHM.TK thing

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
#CHECK IF THIS IS EFFICIENT !!!
def isPrime(number):

    #does a loop from 2 to number and checks for mod
    for x in range(2, number):
        remainder = number % x

        #returns False as soon as divisor is found
        if remainder == 0:
            return False

    #returns True if there is no divisor
    return True

#Perfect Divisor Generator
#NEED TO FIND NUMBERS THAT CANNOT BE THE SUM OF TWO ABUNDANT NUMBERS
#Find Effieciencies for big numbers
def perfectDivisors(n):
    list_1 = []
    condition = True
    start = 1
    stop = 9

    while condition == True:
        for x in range(start, stop):
            #adds perfect divisors to list
            if n % x == 0:
                list_1.append(x)

            #stops the program if x is greater than n
            if x > n/2:
                condition = False
                break

        start = stop - 1
        stop = stop + 10

    list_1 = set(list_1)

    #Returns set of perfect divisors of a number
    return list_1

#PERMUTATION ALGORITHM, uses a generator to make permutations
#can use this with list() to create arr of permutations
def allPerms(elements):

    if len(elements) <=1:
        yield elements

    else:

        for perm in allPerms(elements[1:]):
            for i in range(len(elements)):
                # nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]

#Checks if number is pandigital
def isPandigital(number):
    #creates two variables, one for string of number one for length
    number = str(number)
    length = len(number)

    #creates array with the length of number 1-n
    list_1 = []
    for x in range(1, length+1):
        list_1.append(x)

    #creates array with the string of number
    list_2 = []
    for x in number:
        new_var = int(x)
        list_2.append(new_var)

    #check condition if both it has numbers of its length within the number
    #returns True or False for each condition
    if set(list_1) <= set(list_2):
        return True

    else:
        return False

#Linked Lists ya know (idk I'll just figure this bit out later)
class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

#Returns boolean value whether two strings are anagrams or not
def isAnagram(firstString, secondString):
    condition = True
    if len(firstString) != len(secondString):
        return False

    else:
        for b in firstString:
            if b not in secondString:
                return False

    return True


#gives you zigzag array
def swap(arr,i,j):
    arr[i],arr[j] = arr[j],arr[i]
def zigZag(arr):
    n = len(arr)
    for i in range(len(arr)-1):
        if not i&1:
            if arr[i] > arr[i+1]:
                swap(arr,i,i+1)
        elif arr[i] < arr[i+1]:
            swap(arr,i,i+1)
    return arr

#Still needed:
#-Fastest Route algo
#-Grid algorithm, (returns cartesian plane co-ords upto x, y)
#-Prime Factorizatoin
#-Summend Partitions
#-Greedy Algo's for paths
#-learn what the fuck recursive is

