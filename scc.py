class SCC:
    def __init__(self):
        self.graph = [None]
        self.rgraph = [None]
        self.ftime = None
        self.total = None
        self.finishOrd = []
        self.SCCsizes = []
        self.curLeader = None
        
    def readGraph(self, fname):
        fp = open(fname)
        for line in fp.readlines():
            line = line.split(" ")
            nodeord = int(line[0])
            edgeord = int(line[1])
            if nodeord > len(self.graph)-1:
                i = len(self.graph)
                while i <= nodeord:
                    self.graph.append(self.VNode())
                    i += 1
            self.graph[nodeord].edges.append(edgeord)
        self.total = len(self.graph)-1
        print "graph total = ", self.total
    
    def getRGraph(self):
        for n in range(1, len(self.graph)):
            for e in self.graph[n].edges:
                if e > len(self.rgraph)-1:
                    i = len(self.rgraph)
                    while i <= e:
                        self.rgraph.append(self.VNode())
                        i += 1
                self.rgraph[e].edges.append(n)
        i = len(self.rgraph)
        while i <= self.total:
            self.rgraph.append(self.VNode())
            i += 1
        print "rgraph total = ", len(self.rgraph)-1
    
    class VNode:
        def __init__(self):
            self.edges = []
            self.d = False
            #self.f = None
            #self.h = None

    def DFS_loop1(self, graph):
        self.ftime = 0
        for i in range(1, len(graph)):
            if graph[i].d == False:
                self.DFS1(graph, i)
        #print self.finishOrd
        
    def DFS1(self, graph, i):
        graph[i].d = True
        stack = []
        stack.append(i)
        while len(stack) > 0:
            cur = stack[-1]
            fin = True
            for e in graph[cur].edges:
                if graph[e].d == False:
                    graph[e].d = True
                    stack.append(e)
                    fin = False
                    break
            if fin == True:
                stack.pop()
                self.ftime += 1
                graph[cur].f = self.ftime
                self.finishOrd.append(cur)
        
    def DFS_loop2(self, graph):
        for i in range(len(self.finishOrd)-1, -1, -1):
            node = self.finishOrd[i]
            if graph[node].d == False:
                self.curLeader = node
                #print node
                size = self.DFS2(graph, node)
                self.SCCsizes.append(size)
    
    def DFS2(self, graph, i):
        graph[i].d = True
        stack = []
        stack.append(i)
        size = 0
        while len(stack) > 0:
            cur = stack[-1]
            fin = True
            for e in graph[cur].edges:
                if graph[e].d == False:
                    graph[e].d = True
                    stack.append(e)
                    fin = False
                    break
            if fin == True:
                stack.pop()
                size += 1
        return size
    
    def countSCCs(self, fname):
        self.readGraph(fname)
        self.DFS_loop1(self.graph)
        print max(self.finishOrd)
        self.getRGraph()
        self.graph = []
        self.DFS_loop2(self.rgraph)
        self.SCCsizes.sort(reverse = True)
        print self.SCCsizes[0:10]

def test(fname):
    sol = SCC()
    sol.countSCCs(fname)
    

    