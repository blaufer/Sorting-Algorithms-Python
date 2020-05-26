#----------------------------------------------------------

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

#----------------------------------------------------------

if __name__ == '__main__':
    x = ['a', 'q', 'd', 'f', 'g', 'z', 'x']
    y = bubble_sort(x)
    print(y)
