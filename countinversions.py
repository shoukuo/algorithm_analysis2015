def countInversions(A):
    return mergeCount(A, 0, len(A)-1)
    
def mergeCount(A, l, r):
    if l >= r:
        return 0
    else:
        p = l + (r-l)/2
        cl = mergeCount(A, l, p)
        cr = mergeCount(A, p+1, r)
        cc = merge(A, l, p, r)
        return cl + cr + cc
        
def merge(A, l, p, r):
    count = 0
    tmp = []
    i = l
    j = p+1
    while i <= p and j <= r:
        if A[i] < A[j]:
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            j += 1
            count += p - i + 1
    if i <= p:
        while i <= p:
            tmp.append(A[i])
            i += 1
    if j <= r:
        while j <= r:
            tmp.append(A[j])
            j += 1
    A[l:r+1] = tmp
    return count
        
def test(A):
    print countInversions(A)

#A = [4, 5, 1, 2]
#test(A)
#A = [1, 2]
#test(A)

intarr = []
infile = open("IntegerArray.txt", 'r')
for line in infile:
    intarr.append(int(line))
test(intarr)