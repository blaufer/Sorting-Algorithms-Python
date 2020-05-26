#----- Bubble Sort ----------------------------------------

def bubble_sort(x):
    for i in range(len(x)):
        swap = False
        for j in range(len(x)-1,i+1,-1):
            if x[j] < x[j-1]:
                x[j], x[j-1] = x[j-1], x[j]
                swap = True
        if not swap:
            break

    return x

#---- Heap Sort -------------------------------------------

def heapify(x, n, i): 
    largest = i 
    l = 2 * i + 1 
    r = 2 * i + 2 

    if l < n and x[i] < x[l]:
        largest = l

    if r < n and x[largest] < x[r]:
        largest = r

    if largest != i:
        x[i],x[largest] = x[largest],x[i]

        heapify(x, n, largest)

def heap_sort(x):
    n = len(x)

    for i in range(n, -1, -1):
        heapify(x, n, i)

    for i in range(n-1, 0, -1):
        x[i], x[0] = x[0], x[i]
        heapify(x, i, 0)

    return x

#----- Insertion Sort -------------------------------------

def insertion_sort(x):
    for i in range(1,len(x)):
        key = x[i]
        j = i-1
        while j >= 0 and key < x[j]:
            x[j+1] = x[j]
            j -= 1
        x[j+1] = key

    return x

#----- Merge Sort -----------------------------------------

def merge_sort(x):
    if len(x) >1:
        mid = len(x)//2
        L = x[:mid]
        R = x[mid:]

        merge_sort(L) 
        merge_sort(R) 

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                x[k] = L[i]
                i+=1
            else:
                x[k] = R[j]
                j+=1
            k+=1

        while i < len(L):
            x[k] = L[i]
            i+=1
            k+=1

        while j < len(R):
            x[k] = R[j]
            j+=1
            k+=1

    return x

#----- Quick Sort -----------------------------------------

def partition(x,low,high): 
    i = (low-1) 
    pivot = x[high] 

    for j in range(low, high):
        if x[j] <= pivot:
            i = i+1
            x[i], x[j] = x[j], x[i]

    x[i+1], x[high] = x[high], x[i+1]
    
    return (i+1)

def quick_sort(x, low=None, high=None):
    if low == None:
        low = 0
    if high == None:
        high = len(x)-1

    if low < high:
        pi = partition(x,low, high)
        quick_sort(x, low, pi-1)
        quick_sort(x, pi+1, high)

#----- Selection Sort -------------------------------------

def selection_sort(x):
    for i in range(len(x)):
        k = i
        for j in range(i+1,len(x)):
            if x[j] < x[k]:
                k = j
        x[i], x[k] = x[k], x[i]

    return x

#----- Shell Sort -----------------------------------------

def shell_sort(x):
    n = len(x) 
    gap = n//2

    while gap > 0: 
        for i in range(gap,n): 
            temp = x[i]
            j = i
            
            while j >= gap and x[j-gap] > temp:
                x[j] = x[j-gap]
                j -= gap
            
            x[j] = temp
        
        gap //= 2

    return x

#----------------------------------------------------------

if __name__ == '__main__': 
    from time import time
    from numpy import mean
    from random import randint

    x = [randint(0,1000000) for i in range(900)]

    #x = ['a', 'q', 'd', 'f', 'g', 'z', 'x']
    
    t_list = []
    for i in range(5):
        z = time()
        bubble_sort(x)
        t_list.append(time() - z)
    print('Bubble sort:\t{:e}'.format(mean(t_list)))
    
    t_list = []
    for i in range(5):
        z = time()
        heap_sort(x)
        t_list.append(time() - z) 
    print('Heap sort:\t{:e}'.format(mean(t_list)))
    
    t_list = []
    for i in range(5):
        z = time()
        insertion_sort(x)
        t_list.append(time() - z) 
    print('Insertion sort:\t{:e}'.format(mean(t_list)))
    
    t_list = []
    for i in range(5):
        z = time()
        merge_sort(x)
        t_list.append(time() - z) 
    print('Merge sort:\t{:e}'.format(mean(t_list)))
    
    t_list = []
    for i in range(5):
        z = time()
        quick_sort(x)
        t_list.append(time() - z) 
    print('Quick sort:\t{:e}'.format(mean(t_list)))
    
    t_list = []
    for i in range(5):
        z = time()
        selection_sort(x)
        t_list.append(time() - z) 
    print('Selection sort:\t{:e}'.format(mean(t_list)))
    
    t_list = []
    for i in range(5):
        z = time()
        shell_sort(x)
        t_list.append(time() - z) 
    print('Shell sort:\t{:e}'.format(mean(t_list)))
