import sys
import os
import time

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
def guessNumber(numList):
    
    mid = numList[len(numList) // 2 - 1]
    print(f'Is your number {mid}? Please type Yes or No')
    x = input()
    print(f'The size of the input is {sys.getsizeof(x)} bytes')
    if x == 'Y' or x == 'Yes' or x == 'yes' or x == 'y':
        print(f"GG, your number is {mid}")
        
    else:
        print("Is it higher or lower?")
        x = input()
        
        if x == 'higher' or x == 'Higher':
            newNums = numList[mid:]
            
            return guessNumber(numList[numList.index(mid + 1):])
        
        else:
            
            newNums = numList[:numList.index(mid)]
            print(len(newNums))
            return guessNumber(newNums)

newList = []
i = 0
# while i < 10000:
    
#     i += 1
#     newList.append(i)

print(f'The size of the list I used is {sys.getsizeof(newList)} bytes')
print("Hello! Pick a number between 1 and 10000")
# guessNumber(newList)
# print(sys.getsizeof(guessNumber(newList)))

with open(os.path.join(__location__, 'studentList.txt')) as students:
    x = students.readlines()
    studentList = []
    i = 1
    
    for line in x:
        
        newDict = {}
        values = [item.strip() for item in line.split(',')]
        
        j = 0
        for item in values:
            newDict[values[j]] = values[j + 1]
            values.remove(values[j + 1])
            j += 1
        
        studentList.append(newDict)

def selectionSort(studentList, sortMethod):

    if sortMethod == 'id':
        
        i = 0
        
        # Iterate through list
        while i < len(studentList):
            
            # Set minimum to current index
            minID = studentList[i]

            for student in range(i + 1, len(studentList)):

                # Search for the minimum student ID
                if(int(studentList[student]['studentID']) < int(minID['studentID'])):

                    minID = studentList[student]
            
            # Checks to see if the current index is the minimum. Otherwise, swap
            if studentList[i] == minID:
                i += 1
                pass
                
            else:
                temp = studentList[i]
                changeIndex = studentList.index(minID)
                studentList[i] = studentList[changeIndex]
                studentList[changeIndex] = temp
                i += 1
                
    else:
        i = 0
        
        # Iterate through list
        while i < len(studentList):
            
            # Set minimum to current index
            minID = studentList[i]

            for student in range(i + 1, len(studentList)):

                # Search for the minimum student ID
                if(studentList[student]['firstName'] < minID['firstName']):

                    minID = studentList[student]
            
            # Checks to see if the current index is the minimum. Otherwise, swap
            if studentList[i] == minID:
                i += 1
                pass
                
            else:
                temp = studentList[i]
                changeIndex = studentList.index(minID)
                studentList[i] = studentList[changeIndex]
                studentList[changeIndex] = temp
                i += 1
    
    result = open(r'C:\Users\Jacob\Documents\GitHub\school\Data Structures\Lab_4\sortedStudents.txt', 'w')
        
    for i in studentList:
        result.write(f'{i}\n')
    
    result.close()
    return studentList


def insertionSort(studentList, sortMethod):

    if sortMethod == 'id':
        
        # Iterate over list
        for student in range(1, len(studentList)):
            
            key = studentList[student]

            i = student - 1

            # Checks to see if there needs to be a swap, then swaps until the element is in the right place
            while i >= 0 and int(key['studentID']) < int(studentList[i]['studentID']):

                studentList[i + 1] = studentList[i]
                i -= 1

            studentList[i + 1] = key

        printAll(studentList)
        return studentList
    
    else:
        
        for student in range(1, len(studentList)):
            
            key = studentList[student]

            i = student - 1

            # Checks to see if there needs to be a swap, then swaps until the element is in the right place
            while i >= 0 and key['firstName'] < studentList[i]['firstName']:

                studentList[i + 1] = studentList[i]
                i -= 1

            studentList[i + 1] = key

        printAll(studentList)
    
    result = open(r'C:\Users\Jacob\Documents\GitHub\school\Data Structures\Lab_4\sortedStudents.txt', 'w')
        
    for i in studentList:
        result.write(f'{i}\n')
    
    result.close()
    return studentList

def bubbleSort(studentList, sortMethod):

    # Grabs the length, then initiates a "swapped" bool, for optimization
    length = len(studentList)

    swapped = False

    if sortMethod == 'id':

    # Iterates through the whole list, comparing the current element to the one in front of it
        for i in range(length - 1):

            for swig in range(0, length - i - 1):

                if(int(studentList[swig]['studentID']) > int(studentList[swig + 1]['studentID'])):

                    swapped = True

                    temp = studentList[swig]
                    studentList[swig] = studentList[swig + 1]
                    studentList[swig + 1] = temp

            if not swapped:
                pass

    else:

        for i in range(length - 1):

            for swig in range(0, length - i - 1):

                if(studentList[swig]['firstName'] > studentList[swig + 1]['firstName']):

                    swapped = True

                    temp = studentList[swig]
                    studentList[swig] = studentList[swig + 1]
                    studentList[swig + 1] = temp

            if not swapped:
                pass

    result = open(r'C:\Users\Jacob\Documents\GitHub\school\Data Structures\Lab_4\sortedStudents.txt', 'w')
        
    for i in studentList:
        result.write(f'{i}\n')
    
    result.close()
    printAll(studentList)
    return studentList

def mergeSort(studentList, sortMethod):

    if len(studentList) > 1:

        # Slice the list in two

        mid = len(studentList) // 2

        leftList = studentList[ : mid]

        rightList = studentList[ mid : ]

        # Call each side recursively

        mergeSort(leftList, sortMethod)
        mergeSort(rightList, sortMethod)

        # Indices
        i = 0
        j = 0
        k = 0

        if sortMethod == 'id':

            # Building each side of the list depending on which number is bigger
            while i < len(leftList) and j < len(rightList):

                if int(leftList[i]['studentID']) <= int(rightList[j]['studentID']):

                    studentList[k] = leftList[i]
                    i = i + 1

                else:

                    studentList[k] = rightList[j]
                    j = j + 1

                k = k + 1

            # Catches for odd length lists
            while i < len(leftList):

                studentList[k] = leftList[i]
                i = i + 1
                k = k + 1

            while j < len(rightList):

                studentList[k] = rightList[j]
                j = j + 1
                k = k + 1

        else:
            # Building each side of the list depending on which number is bigger
            while i < len(leftList) and j < len(rightList):

                if leftList[i]['firstName'] <= rightList[j]['firstName']:

                    studentList[k] = leftList[i]
                    i = i + 1

                else:

                    studentList[k] = rightList[j]
                    j = j + 1

                k = k + 1

            # Catches for odd length lists
            while i < len(leftList):

                studentList[k] = leftList[i]
                i = i + 1
                k = k + 1

            while j < len(rightList):

                studentList[k] = rightList[j]
                j = j + 1
                k = k + 1

    result = open(r'C:\Users\Jacob\Documents\GitHub\school\Data Structures\Lab_4\sortedStudents.txt', 'w')

    if len(studentList) == 20:    
        for i in studentList:
            result.write(f'{i}\n')
        
        result.close()
        printAll(studentList)
        return studentList

def printAll(studentList):
    

    for student in studentList:
        print(student)

start = float(time.time() * 1000)

print(selectionSort(studentList, 'id').__sizeof__())
print(insertionSort(studentList, 'id').__sizeof__())
print(bubbleSort(studentList, 'id').__sizeof__())
print(mergeSort(studentList, 'id').__sizeof__())


end = float(time.time() * 1000)

result = end - start

print(f'Operation took {result} milliseconds')