# CMPSC Lab 2
# Searching and Sorting

import json
import random
import time

# Read text file and store
jsonFile = open(r'C:\Users\Jacob\Documents\School\Data Structures\Lab_2\students.txt')
sameFile = open(r'C:\Users\Jacob\Documents\School\Data Structures\Lab_2\allSame.txt')
sameStudents = json.load(sameFile)
students = json.load(jsonFile)
studentList = students['Students']
sameList = sameStudents['Students']

searchID = random.randint(1, 20)

# For linear and binary search, I took the dictionary with one key and the value of a list of dictionaries. 
# I am too lazy to change this, though I know it was a silly thing to do.

def linearSearch(studentIDNumber, studentList):
    
    # Iterate through the students dictionary, searching for the correct ID
    for student in studentList['Students']:

        # If found, print
        if (studentIDNumber == student['studentID']):

            returnName = student['firstName']
            print(f'Student ID {studentIDNumber} was found, their name is {returnName}')

            return student

    # Catch bad ID
    return 'Student not found'


def binarySearch(studentIDNumber, studentList):
    
    # Checks base case of only one student in the list
    if(len(studentList['Students']) == 1):

        foundStudent = studentList['Students'][0]
        studentName = foundStudent['firstName']

        if(foundStudent['studentID'] == studentIDNumber):

            print(f'Student ID {studentIDNumber} was found, their name is {studentName}')
            
            return foundStudent
        
        # Catches bad ID
        else:

            print(f'Student ID {studentIDNumber} not found.')
            return

    # Set middle of current list, then check to see if it matches what we want
    mid = len(studentList['Students']) // 2

    check = studentList['Students'][mid]

    if (check['studentID'] == studentIDNumber):

        studentName = check['firstName']
        print(f'Student ID {studentIDNumber} was found, their name is {studentName}') 
        return check

    # Slices the list at the middle, only searches the half with the ID in it
    if(studentIDNumber > check['studentID']):

        newStudents = {'Students' : studentList['Students'][mid + 1:]}

    else:

        newStudents = {'Students' : studentList['Students'][:mid]}
    
    # Recursive call with sliced list
    return binarySearch(studentIDNumber, newStudents)


def selectionSort(studentList):

    i = 0
    
    # Iterate through list
    while i < len(studentList):
        
        # Set minimum to current index
        minID = studentList[i]

        for student in range(i + 1, len(studentList)):

            # Search for the minimum student ID
            if(studentList[student]['studentID'] < minID['studentID']):

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

    printAll(studentList)
    return studentList


def insertionSort(studentList):

    # Iterate over list
    for student in range(1, len(studentList)):
        
        key = studentList[student]

        i = student - 1

        # Checks to see if there needs to be a swap, then swaps until the element is in the right place
        while i >= 0 and key['studentID'] < studentList[i]['studentID']:

            studentList[i + 1] = studentList[i]
            i -= 1

        studentList[i + 1] = key

    printAll(studentList)
    return studentList

     

def bubbleSort(studentList):

    # Grabs the length, then initiates a "swapped" bool, for optimization
    length = len(studentList)

    swapped = False

    # Iterates through the whole list, comparing the current element to the one in front of it
    for i in range(length - 1):

        for swig in range(0, length - i - 1):

            if(studentList[swig]['studentID'] > studentList[swig + 1]['studentID']):

                swapped = True

                temp = studentList[swig]
                studentList[swig] = studentList[swig + 1]
                studentList[swig + 1] = temp

        if not swapped:
            pass

    printAll(studentList)
    return studentList

def mergeSort(studentList):

    if len(studentList) > 1:

        # Slice the list in two

        mid = len(studentList) // 2

        leftList = studentList[ : mid]

        rightList = studentList[ mid : ]

        # Call each side recursively

        mergeSort(leftList)
        mergeSort(rightList)

        # Indices
        i = 0
        j = 0
        k = 0

        # Building each side of the list depending on which number is bigger
        while i < len(leftList) and j < len(rightList):

            if leftList[i]['studentID'] <= rightList[j]['studentID']:

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

    printAll(studentList)
    return studentList

def printAll(studentList):
    

    for student in studentList:
        print(student)

start = float(time.time() * 1000)

# linearSearch(searchID, students)
# binarySearch(searchID, students)
# selectionSort(sameList)
# insertionSort(studentList)
bubbleSort(studentList)
# mergeSort(studentList)

end = float(time.time() * 1000)

result = end - start

print(f'Operation took {result} milliseconds')