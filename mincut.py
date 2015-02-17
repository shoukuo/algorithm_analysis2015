import random
def mincut(graph):
    num = len(graph)
    for i in range(0, num-2):
        #print "graph len = ", len(graph)
        rand1 = random.randint(0, len(graph)-1)
        entry = graph[rand1]  
        us = entry[0]
        #print us
        ##print graph[rand1]
        rand2 = random.randint(0, len(entry[1])-1)
        v = entry[1][rand2]
        for r in range(0, len(graph)):
            if v in graph[r][0]:
                break   
        vs = graph[r][0]
        uvs =  us + vs
           
        tmp = entry[1][:]
        entry[1] = []
        for e in tmp:
            if not e in vs:
                entry[1].append(e)
        ##print rand2

        for adj in graph[r][1]:
            if not adj in us:
                entry[1].append(adj)
                
        graph[r] = graph[-1]
        del graph[-1]
        entry[0] = uvs
     
    return len(graph[0][1])   
    #print "graph len = ", len(graph)
    #print graph[0][1]
    
def test():
    fp = open("kargerMinCut.txt")
    graph = []
    for line in fp.readlines():
        line = line.split("\t")
        graph.append([[line[0]], line[1:-1]])

    mincuts = 100000
    for i in range(0, 10000):
        tmp = mincut(graph)
        if tmp < mincuts:
            mincuts = tmp
    print "mincuts = ", mincuts
test()
    
        