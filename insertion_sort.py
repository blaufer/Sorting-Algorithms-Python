#----------------------------------------------------------

def insertion_sort(x):
    for i in range(1,len(x)):
        key = x[i]
        j = i-1
        while j >= 0 and key < x[j]:
            x[j+1] = x[j]
            j -= 1
        x[j+1] = key

    return x

#----------------------------------------------------------

if __name__ == '__main__':
    x = ['a', 'q', 'd', 'f', 'g', 'z', 'x']
    y = insertion_sort(x)
    print(y)
