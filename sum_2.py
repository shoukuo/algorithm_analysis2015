def bsearch(data, left, right, key, mod):
    if left > right:
        if mod == 0:
            return -1
        elif mod == 1:
            return right+1
        else:
            return left-1
    mid = left + (right-left)/2
    if data[mid] == key:
        return mid
    elif data[mid] < key:
        return bsearch(data, mid+1, right, key, mod)
    else:
        return bsearch(data, left, mid-1, key, mod)    
          
def sum_2(fname):
    print fname
    fp = open(fname)
    data = []
    for line in fp.readlines():
        data.append(int(line))
    data.sort()
    sums = []
    for x in data:
        l = bsearch(data, 0, len(data)-1, -10000-x, 1)
        r = bsearch(data, 0, len(data)-1, 10000-x, 2)
        #print x, l, r
        for i in range(l, r+1):
            sums.append(x+data[i])
    return sums

sums =  sum_2("2sum.txt")
#sums = sum_2("sumtest1.txt")
dic = {}
for n in sums:
    dic[n] = 1
print len(dic)

    
