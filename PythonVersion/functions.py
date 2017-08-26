from math import *
import math

#Collection of Functions that can prove useful in competetive coding


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

#swaps two elements in a given array
#needs arr arguements as well as two indexes
def swap(arr,i,j):
    arr[i],arr[j] = arr[j],arr[i]

#gives you zigzag array
def zigZag(arr):

    n = len(arr)
    for i in range(len(arr)-1):
        if not i&1:
            if arr[i] > arr[i+1]:

                #functions that swaps two items in an array
                swap(arr,i,i+1)
        elif arr[i] < arr[i+1]:
            swap(arr,i,i+1)
    return arr

#RETURNS SUM OF DIAGONALS OF A GIVEN 2DARRAY
def diagonalSum(array):
    sizeArray = len(array[0])
    leftDiagonal = 0
    rightDiagonal = 0

    for x in range(sizeArray):
        leftDiagonal += array[x][x]
        rightDiagonal += array[x][sizeArray-1-x]

    return(leftDiagonal+rightDiagonal)

def diagonalDiff(array):
    def diagonalSum(array):
        sizeArray = len(array[0])
        leftDiagonal = 0
        rightDiagonal = 0

        for x in range(sizeArray):
            leftDiagonal += array[x][x]
            rightDiagonal += array[x][sizeArray - 1 - x]

        return (abs(leftDiagonal - rightDiagonal))

#https://en.wikipedia.org/wiki/Change-making_problem
def _get_change_making_matrix(set_of_coins, r):
      m = [[0 for _ in range(r + 1)] for _ in range(len(set_of_coins) + 1)]
  
      for i in range(r + 1):
          m[0][i] = i
  
      return m
  
  def change_making(coins, n):
     """This function assumes that all coins are available infinitely.
 
     n is the number that we need to obtain with the fewest number of coins.
 
     coins is a list or tuple with the available denominations."""
 
     m = _get_change_making_matrix(coins, n)
 
     for c in range(1, len(coins) + 1):
 
         for r in range(1, n + 1):
 
             # Just use the coin coins[c - 1].
             if coins[c - 1] == r:
                 m[c][r] = 1
 
             # coins[c - 1] cannot be included.
             # We use the previous solution for making r,
             # excluding coins[c - 1].
             elif coins[c - 1] > r:
                 m[c][r] = m[c - 1][r]
 
             # We can use coins[c - 1].
             # We need to decide which one of the following solutions is the best:
             # 1. Using the previous solution for making r (without using coins[c - 1]).
             # 2. Using the previous solution for making r - coins[c - 1] (without using coins[c - 1]) plus this 1 extra coin.
             else:
                 m[c][r] = min(m[c - 1][r], 1 + m[c][r - coins[c - 1]])
 
     return m[-1][-1]

#Still needed:
#-Fastest Route algo
#-Grid algorithm, (returns cartesian plane co-ords upto x, y)
#-Summend Partitions
#-Greedy Algo's for paths
#-learn what the fuck recursive is
