

def quickSort(A, p, r):
    
    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q - 1)
        quickSort(A, q + 1, r)
    
def partition(A, p, r):
    
    x = A[r]
    i = p - 1
    j = p
    
    for j in range(p, r):
        
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
            
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

test = [5, 7, 9, 2, 3, 123, 532, 6, 21, 324, 5, 6, 362]
test2 = [2, 5, 7, 8, 65, 47, 654, 387654,32]
test3 = ['j', 'a', 'd', 'b', 'z'] 
quickSort(test, 0, len(test) - 1)
quickSort(test2, 0, len(test2) - 1)
quickSort(test3, 0, len(test3) - 1)
print(test)   
print(test2)
print(test3)