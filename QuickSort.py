#q1 162085

def Exch(A, i, j):
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp
    
def Partition(A, l, r):
    i = l+1
    j = l+1
    while j <= r:
        if A[j] < A[l]:
            Exch(A, i, j)
            i += 1
        j += 1
    i -= 1
    Exch(A, l, i)
    return i
    
def QuickSort(A, l, r):
    if l >= r:
        return 0
    
    p = Partition(A, l, r)
    nl = QuickSort(A, l, p-1)
    nr = QuickSort(A, p+1, r)
    return nl + nr + (r-l)

print 1 
ftxt = open("QuickSort.txt")
array = []
for line in ftxt.readlines():
    array.append(int(line))
print QuickSort(array, 0, len(array)-1)
    
