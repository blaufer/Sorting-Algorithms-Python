#----------------------------------------------------------

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
    x = ['a', 'q', 'd', 'f', 'g', 'z', 'x']
    y = shell_sort(x)
    print(y)
