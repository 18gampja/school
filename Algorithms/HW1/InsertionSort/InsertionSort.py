import random

def insertionSort(arr):
    
    for i in range(len(arr)):
        index = arr[i]
        j = i - 1
        
        while j >= 0 and index < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            
        arr[j + 1] = index
    
    return arr
        
def generateArray():
    
    newList = []
    listLength = random.randint(3, 10)
    
    for i in range(listLength + 1):
        newList.append(random.randint(1, 100))
        
    print(f'Unsorted list: {newList}')
    return newList

print(f'Sorted list: {insertionSort(generateArray())}')      