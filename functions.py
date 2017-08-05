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

#Greatest Common Divisor tool is in standard library
#Just use gcd(x,y) and it returns gcd
#lowest common multiple however
def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b / gcd(a, b)

#returns 2d array with co-ords up to limit of x, y
def grid(x, y):
    arr = []
    for x in range(x+1):
        for b in range(y+1):
            point = [x, b]
            arr.append(point)

    return arr


def isPalindrome(num):
    if num[::-1] == num:
        return True

    else:
        return False


#Prints possibility of sets that create the target
#Takes numbers as a list, targer as an integer
#Finessed from: https://stackoverflow.com/questions/4632322/finding-all-possible-combinations-of-numbers-to-reach-a-given-sum
def subset_sum(numbers, target, partial=[]):
    s = sum(partial)

    # check if the partial sum is equals to target
    if s == target:
        print("sum(%s)=%s" % (partial, target))
    if s >= target:
        return  # if we reach the number why bother to continue

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        subset_sum(remaining, target, partial + [n])



#Dijkstra's Algorithm
#Taken from: https://gist.github.com/econchick/4666413
class Graph:
  def __init__(self):
    self.nodes = set()
    self.edges = defaultdict(list)
    self.distances = {}

  def add_node(self, value):
    self.nodes.add(value)

  def add_edge(self, from_node, to_node, distance):
    self.edges[from_node].append(to_node)
    self.edges[to_node].append(from_node)
    self.distances[(from_node, to_node)] = distance


def dijsktra(graph, initial):
  visited = {initial: 0}
  path = {}

  nodes = set(graph.nodes)

  while nodes:
    min_node = None
    for node in nodes:
      if node in visited:
        if min_node is None:
          min_node = node
        elif visited[node] < visited[min_node]:
          min_node = node

    if min_node is None:
      break

    nodes.remove(min_node)
    current_weight = visited[min_node]

    for edge in graph.edges[min_node]:
      weight = current_weight + graph.distance[(min_node, edge)]
      if edge not in visited or weight < visited[edge]:
        visited[edge] = weight
        path[edge] = min_node

  return visited, path


#Or This implementation of Dijkstra's
nodes = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
distances = {
    'B': {'A': 5, 'D': 1, 'G': 2},
    'A': {'B': 5, 'D': 3, 'E': 12, 'F' :5},
    'D': {'B': 1, 'G': 1, 'E': 1, 'A': 3},
    'G': {'B': 2, 'D': 1, 'C': 2},
    'C': {'G': 2, 'E': 1, 'F': 16},
    'E': {'A': 12, 'D': 1, 'C': 1, 'F': 2},
    'F': {'A': 5, 'E': 2, 'C': 16}}

unvisited = {node: None for node in nodes} #using None as +inf
visited = {}
current = 'B'
currentDistance = 0
unvisited[current] = currentDistance

while True:
    for neighbour, distance in distances[current].items():
        if neighbour not in unvisited: continue
        newDistance = currentDistance + distance
        if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
            unvisited[neighbour] = newDistance
    visited[current] = currentDistance
    del unvisited[current]
    if not unvisited: break
    candidates = [node for node in unvisited.items() if node[1]]
    current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]

print(visited)



#Still needed:
#-Fastest Route algo
#-Grid algorithm, (returns cartesian plane co-ords upto x, y)
#-Summend Partitions
#-Greedy Algo's for paths
#-learn what the fuck recursive is
