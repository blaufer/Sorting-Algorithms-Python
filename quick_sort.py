#----------------------------------------------------------

def partition(x,low,high): 
    i = (low-1) 
    pivot = x[high] 

    for j in range(low, high):
        if x[j] <= pivot:
            i = i+1
            x[i], x[j] = x[j], x[i]

    x[i+1], x[high] = x[high], x[i+1]
    
    return (i+1)

#----------------------------------------------------------

def quick_sort(x, low=None, high=None):
    if low == None:
        low = 0
    if high == None:
        high = len(x)-1

    if low < high:
        pi = partition(x,low, high)
        quick_sort(x, low, pi-1)
        quick_sort(x, pi+1, high)

#----------------------------------------------------------

if __name__ == '__main__':
    x = ['a', 'q', 'd', 'f', 'g', 'z', 'x']
    quick_sort(x)
    print(x)
