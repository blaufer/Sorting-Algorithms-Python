#----------------------------------------------------------

def selection_sort(x):
    for i in range(len(x)):
        k = i
        for j in range(i+1,len(x)):
            if x[j] < x[k]:
                k = j
        x[i], x[k] = x[k], x[i]

    return x

#----------------------------------------------------------

if __name__ == '__main__':
    x = ['a', 'q', 'd', 'f', 'g', 'z', 'x']
    y = selection_sort(x)
    print(y)
