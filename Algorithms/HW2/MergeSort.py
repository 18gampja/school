import random

def mergeSortDAC(arr):

    if len(arr)>1:

        mid = len(arr) // 2

        leftList = arr[ : mid]

        rightList = arr[ mid : ]

        mergeSortDAC(leftList)
        mergeSortDAC(rightList)

        i = 0
        j = 0
        k = 0

        while i < len(leftList) and j < len(rightList):

            if leftList[i] <= rightList[j]:

                arr[k]=leftList[i]
                i=i+1

            else:

                arr[k]=rightList[j]
                j=j+1

            k=k+1

        while i < len(leftList):

            arr[k]=leftList[i]
            i=i+1
            k=k+1

        while j < len(rightList):

            arr[k]=rightList[j]
            j=j+1
            k=k+1

    print(f'The list right now is {arr}')


def genList(length):

    newList = []
    count = 0

    while count < length:
        newList.append(random.randint(1, 10000))
        count += 1

    return newList

arr = genList(100)

print(f'Original list is {arr}')

mergeSortDAC(arr)
print(arr)