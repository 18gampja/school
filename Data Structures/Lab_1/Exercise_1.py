import random
import time

# Creates the list and dictionary for trials
count = 0
intList = []
intDict = {}

while count < 10000:
       x = random.randint(0, 10000)
       
       intList.append(x)
       intDict[x] = count
       
       count += 1

# Just prints the list and dictionary
def printList():
    
    start = time.time()
    print(intList)
    end = time.time()
    print("Total time taken to print is: " + str(end - start))
    
def printDict():
    
    start = time.time()
    print(intDict)
    end = time.time()
    print("Total time taken to print is: " + str(end - start))
    
# Finds a random value
def findRand():
    
    x = random.randint(0, 10000)
    
    start = time.time()
    print("Does the list contain " + str(x) + ": " + str(intList.__contains__(x)))
    end = time.time()
    
    print("Total time to find is: " + str(end - start))
    print()
    
    start = time.time()
    print("Does the dictionary contain " + str(x) + ": " + str(intDict.__contains__(x)))
    end = time.time()
    
    print("Total time to find is: " + str(end - start))
    print()
    
# Inserts a random value to index 300
def insertRand():
    
    x = random.randint(0, 10000)
    
    start = time.time()
    intList.insert(x, 300)
    print(intList)
    end = time.time()
    
    listTime = str(end - start)
    
    start = time.time()
    intDict[300] = x
    print(intDict)
    end = time.time()
    
    dictTime = str(end - start)
    
    print("List time is: " + listTime)
    print("Dictionary time is: " + dictTime)
    
# Deletes a random variable
def deleteRand():
    
    x = random.randint(0, 10000)
    
    start = time.time()
    if x in intList:
        print("Value in list.")
        intList.remove(x)
    
    else:
        print("Value not in list.")
    end = time.time()
    
    listTime = str(end - start)
    
    start = time.time()
    if x in intDict.keys():
        print("Value in dict.")
        intDict.pop(x, intDict[x])
    
    else:
        print("Value not in dict")
    end = time.time()
    
    dictTime = str(end - start)
    print("Time taken for list operation: " + listTime)
    print("Time taken for dictionary operation: " + dictTime)

# The actual methods for demonstration
printList()
# printDict()
# findRand()
# insertRand()
# deleteRand()