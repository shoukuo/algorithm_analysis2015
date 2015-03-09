class MinPQ:
    def __init__(self):
        self.data = [None]
    
    def size(self):
        return len(self.data)-1
        
    def insert(self, val):
        self.data.append(val)
        self.bubble_up(len(self.data)-1)

        
    def bubble_up(self, posi):
        while posi > 1:
            if self.less(posi, posi/2):
                self.exch(posi, posi/2)
                posi = posi/2
            else:
                break
    def exch(self, i, j):
        tmp = self.data[i]
        self.data[i] = self.data[j]
        self.data[j] = tmp
    
    def min(self):
        return self.data[1]
    
    def extract_min(self):
        minval = self.data[1]
        self.exch(1, len(self.data)-1)
        del self.data[-1]
        self.bubble_down(1)
        return minval
        
    def less(self, i, j):
        if self.data[i] < self.data[j]:
            return True
        else:
            return False
            
    def bubble_down(self, posi):
        while posi*2 <= len(self.data)-1:
            j = posi * 2
            if j < len(self.data)-1 and self.less(j+1, j):
                j += 1
            if not self.less(j, posi):
                break
            self.exch(posi, j)
            posi = j

class MaxPQ:
    def __init__(self):
        self.data = [None]
    
    def size(self):
        return len(self.data)-1
    
    def insert(self, val):
        self.data.append(val)
        self._bubble_up(len(self.data)-1)
        
    def _bubble_up(self, posi):
        while posi > 1:
            if self._less(posi/2, posi):
                self._exch(posi, posi/2)
                posi = posi/2
            else:
                break
                
    def _exch(self, i, j):
        tmp = self.data[i]
        self.data[i] = self.data[j]
        self.data[j] = tmp
    
    def max(self):
        return self.data[1]
        
    def extract_max(self):
        maxval = self.data[1]
        self._exch(1, len(self.data)-1)
        del self.data[-1]
        self._bubble_down(1)
        return maxval       
        
    def _less(self, i, j):
        if self.data[i] < self.data[j]:
            return True
        else:
            return False
            
    def _bubble_down(self, posi):
        while posi*2 <= len(self.data)-1:
            j = posi * 2
            if j < len(self.data)-1 and self._less(j, j+1):
                j += 1
            if not self._less(posi, j):
                break
            self._exch(posi, j)
            posi = j  
            
class Median:
    def __init__(self):
        self._minpq = MinPQ()
        self._maxpq = MaxPQ()
        
    def _adjust(self):
        while self._maxpq.size() <= self._minpq.size():
            self._maxpq.insert(self._minpq.extract_min())
        while self._maxpq.size() > self._minpq.size()+1:
            self._minpq.insert(self._maxpq.extract_max())
            
    def medians(self, fname):
        fp = open(fname)
        medians = []
        number = int(fp.readline())
        self._maxpq.insert(number)
        medians.append(self._maxpq.max())
        
        for line in fp.readlines():
            number = int(line)
            if self._maxpq.size() <= 0 or number < self._maxpq.max():
                self._maxpq.insert(number)
            else:
                self._minpq.insert(number)
            self._adjust()
            #print "MinPQ", self._minpq.data
            #print "MaxPQ", self._maxpq.data
            #print self._maxpq.max()
            medians.append(self._maxpq.max())
        return medians
    
def test(fname):
    sol = Median()
    print sum(sol.medians(fname))%10000
#test("mediantest1.txt")
#test("mediantest2.txt")
#test("mediantest3.txt")
test("Median.txt")            
        
    