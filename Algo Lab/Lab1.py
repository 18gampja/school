import time
import random
import sys

def gcd(num1, num2):

    # We start with minimum just in case number 1 is a divisor for number 2, or vice versa
    result = min(num1, num2)

    # Check to see if it's a common divisor, breaking on the first one we find
    while result:
        if num1 % result == 0 and num2 % result == 0:
            break
        result -= 1

    return result

# testA = random.randint(0, 1000000)
# testB = random.randint(0, 1000000)

# start = int(round(time.time() * 10000))
# result = gcd(testA, testB)
# end = int(round(time.time() * 10000))

# total = end - start

# print(f'It took {total} milliseconds to find that {result} is the gcd of {testA} and {testB}.')

def findMinMax(arr):

    arrMax = -sys.maxsize
    arrMin = sys.maxsize

    # Checks for an empty list
    if arr == []:
        return('Empty list')

    # Checks to see if the list has only one integer
    elif len(arr) == 0:
        return(arr[0], arr[0])

    # Iterates over the whole list to find the minimum value. Sets minimum to the first integer encountered by default.
    for i in range(len(arr)):

        if(arr[i] < arrMin):
            arrMin = arr[i]

        if(arr[i] > arrMax):
            arrMax = arr[i]

    return arrMin, arrMax


def genListSmall():

    newList = []
    count = 0

    while count < 1000:
        newList.append(random.randint(1, 10000))
        count += 1

    return newList

def genListLarge():
    newList = []
    count = 0

    while count < 10000:
        newList.append(random.randint(1, 10000))
        count += 1

    return newList

# test = genListSmall()
# start = int(round(time.time() * 1000))
# listMin, listMax = findMinMax(test)
# end = int(round(time.time() * 1000))

# print(f'It took {end - start} milliseconds to find the max of {listMax} and a min of {listMin} for the list of 1000 integers.')

# test = genListLarge()
# start = int(round(time.time() * 1000))
# listMin, listMax = findMinMax(test)
# end = int(round(time.time() * 1000))

# print(f'It took {end - start} milliseconds to find the max of {listMax} and a min of {listMin} for the list of 10000 integers.')


def findMinMaxDAC(arr, left, right, listMin = sys.maxsize, listMax = -sys.maxsize):

    # Base case that checks to see if the list has only two integers
    if left == right:

        if listMin > arr[right]:
            listMin = arr[right]

        if listMax < arr[left]:
            listMax = arr[left]
        
        return listMin, listMax

    # Base case that handles the end of the recursive stack
    if right - left == 1:

        if arr[left] < arr[right]:
            if listMin > arr[left]:
                listMin = arr[left]

            if listMax < arr[right]:
                listMax = arr[right]

        else:
            if listMin > arr[right]:
                listMin = arr[right]

            if listMax < arr[left]:
                listMax = arr[left]

        return listMin, listMax

    # Finds the middle to bisect the list
    mid = (left + right) // 2

    # Recursively calls the method for the left side of the list
    listMin, listMax = findMinMaxDAC(arr, left, mid, listMin, listMax)

    # Recursively calls the method for the right side of the list
    listMin, listMax = findMinMaxDAC(arr, mid + 1, right, listMin, listMax)

    return listMin, listMax

test = genListSmall()

start = int(round(time.time() * 1000))
(listMin, listMax) = findMinMaxDAC(test, 0, len(test) - 1)
end = int(round(time.time() * 1000))

print(f'It took {end - start} milliseconds to find that the min is {listMin} and the max is {listMax} for the list of 1000 integers using DAC method.')

test = genListLarge()
start = int(round(time.time() * 1000))
(listMin, listMax) = findMinMaxDAC(test, 0, len(test) - 1)
end = int(round(time.time() * 1000))
print(f'It took {end - start} milliseconds to find that the min is {listMin} and the max is {listMax} for the list of 10000 integers using DAC method.')
