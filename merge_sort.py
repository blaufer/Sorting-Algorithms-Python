#----------------------------------------------------------

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

#----------------------------------------------------------

if __name__ == '__main__':
    x = ['a', 'q', 'd', 'f', 'g', 'z', 'x']
    y = merge_sort(x)
    print(y)
