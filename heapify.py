# NOT A CLASS ONLY FUNCTIONS TO HEAPIFY ARRAYS AND SORT USING HEAPSORT 
# heapify an array (USE BUILD HEAP METHOD)

def heapify(array,n,i):
    largest = i
    left = 2*i
    right = 2*i+1
    if left < n and array[largest] > array[left]:
        largest = left
    if right < n and array[largest] > array[right]:
        largest = right
    if largest != i:
        array[i],array[largest] = array[largest],array[i]
        heapify(array,n,largest)

#build heap from an array
def buildHeap(array):
    n = len(array)
    for i in range(int(n/2),-1,-1):
        heapify(array,n,i)
    print(array)
# heap sort            
def heapSort(arr):
    n = len(arr)
    for i in range(n, -1, -1): 
        heapify(arr, n, i) 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] 
        heapify(arr, i, 0) 
    return arr
