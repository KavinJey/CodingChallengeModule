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


