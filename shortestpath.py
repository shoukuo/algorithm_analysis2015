class MinPQ:
    """
    used for Dijstra shortest path
    """
    def __init__(self):
        self.data = [None]
        
    def exch(self, i, j):
        tmp = self.data[i]
        self.data[i] = self.data[j]
        self.data[j] = tmp
        
    def bubble_up(self, posi):
        while posi > 1:
            if self.greater(posi/2, posi):
                self.exch(posi, posi/2)
                posi = posi/2
            else:
                break
                
    def greater(self, i, j):
        if self.data[i][0] > self.data[j][0]:
            return True
        else:
            return False
                
    def insert(self, tu):
        self.data.append(tu)
        self.bubble_up(len(self.data)-1)
    
    def min(self):
        minele = self.data[1]
        self.exch(1, len(self.data)-1)
        del self.data[-1]
        self.bubble_down(1)
        return minele
        
    def bubble_down(self, posi):
        maxposi = len(self.data)-1
        while posi * 2 <= maxposi:
            j = posi * 2
            if (j < maxposi and self.greater(j, j+1)):
                j += 1
            if self.data[posi] <= self.data[j]:
                break
            self.exch(posi, j)
            posi = j
    def findId(self, id):
        for i in range(1, len(self.data)):
            if self.data[i][1] == id:
                return i
        return 0
    
    def setDis(self, posi, d):
        self.data[posi][0] = d
        self.bubble_up(posi)
    
    def getDis(self, posi):
        return self.data[posi][0]

class DijstraPath:
    """
    compute Dijstra Shortest Path
    """
    def __init__(self):
        self.graph = [None]
        self.X = []
        
    class Vertex:
        def __init__(self, n):
            self.id = n
            self.dis = 0
            self.adjs = []
            self.path = []
            
    def readGraph(self, fname, sep = " "):
        fp = open(fname)
        for line in fp.readlines():
            line = line.strip()
            line = line.split(sep)
            vnum = int(line[0])
            v = self.Vertex(vnum)
            for i in range(1, len(line)):
                pair = line[i].split(",")
                v.adjs.append((int(pair[0]), int(pair[1])))
            self.graph.append(v)
            print v.adjs
                        
    def DijstraPath(self, start):
        total = len(self.graph)-1
        mpq = MinPQ()
        self.X.append(start)
        curv = start
        while len(self.X) < total:
            print "len(self.X) = ", len(self.X)
            for e in self.graph[curv].adjs:
                print e
                if not e[0] in self.X:
                    #print e
                    disTmp = self.graph[curv].dis + e[1]
                    posi = mpq.findId(e[0])
                    if posi == 0:  
                        mpq.insert([disTmp, e[0]])
                        self.graph[e[0]].path = self.graph[curv].path + [e[0]] 
                    else:
                        if disTmp < mpq.getDis(posi):
                            mpq.setDis(posi, disTmp)
                            self.graph[e[0]].path = self.graph[curv].path + [e[0]] 
                    print mpq.data
            minele = mpq.min()
            print "min", minele
            v= minele[1]
            self.graph[v].dis = minele[0]
            self.X.append(v)
            curv = v
            
    def shortestPath(self):
        self.DijstraPath(1)
        vs = [7,37,59,82,99,115,133,165,188,197]
        result = ""
        for v in vs:
            result += str(self.graph[v].dis)+str(",")
        print result
                 
def test():
    sol = DijstraPath()       
    sol.readGraph("dijkstraData.txt", sep = "\t")
    sol.shortestPath()
test()