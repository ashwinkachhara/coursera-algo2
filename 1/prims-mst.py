import heapq

class Edge:
    def __init__(self, v1, v2, cost):
        self.v1 = v1
        self.v2 = v2
        self.cost = cost
    def __cmp__(self, other):
        return cmp(self.cost, other.cost)

def readGraph(filename):
    f = open(filename)
    
    [nodes, edges] = f.readline().strip().split(" ")
    nodeNum = int(nodes)
    edgeNum = int(edges)
    
    edges = []
    
    for line in f:
        [v1, v2, cost] = [int(a) for a in line.strip().split(" ")]
        e = Edge(v1, v2, cost)
        edges.append(e)
    return nodeNum, edges
    
# def primMST(edges, nodeNum):
#     V = set(range(1, nodeNum+1))
#     X = set([1])
    
#     edgeHeap = []
#     #print len(edges)
#     for edge in edges:
#         if edge.v1 in X or edge.v2 in X:
#             edgeHeap.append(edge)
#     heapq.heapify(edgeHeap)
#     print len(edgeHeap)
    
    
    
#     treeEdges = []
    
    #numEdg = 0
    
    # while X != V:
    #     #print edges[0]
    #     nextEdge = heapq.heappop(edgeHeap)
    #     numEdg = numEdg + 1
    #     #print str(nextEdge.v1) + ", " + str(nextEdge.v2) + ", " + str(nextEdge.cost)
    #     if nextEdge.v1 in X and nextEdge.v2 not in X:
    #         X.add(nextEdge.v1)
    #         treeEdges.append(nextEdge)
    #     if nextEdge.v2 in X and nextEdge.v1 not in X:
    #         X.add(nextEdge.v2)
    #         treeEdges.append(nextEdge)
    #     #print str(numEdg) + "; " + str(len(X))
    # print len(treeEdges)
    
def getAdjList(edges):
    adjList = {}
    
    for edge in edges:
        if edge.v1 in adjList:
            adjList[edge.v1].append((edge.v2, edge.cost))
        else:
            adjList[edge.v1] = [(edge.v2, edge.cost)]
        if edge.v2 in adjList:
            adjList[edge.v2].append((edge.v1, edge.cost))
        else:
            adjList[edge.v2] = [(edge.v1, edge.cost)]
    return adjList
    
def primHeap(nodeNum, edges):
    adjList = getAdjList(edges)
    
    heap = []
    
    # init the heap
    node = 1
    neighbors = adjList[1]
    for edge in neighbors:
        heapq.heappush(heap, (edge[1], set([edge[0], node])))
    
    X = set([1])
    V = set(range(1,nodeNum+1))
    tree = []
    treeCost = 0
    
    while X!=V:
        cost, verts = heapq.heappop(heap)
        if len(X.intersection(verts)) > 1:
            continue
        tree.append((cost, verts))
        treeCost = treeCost + cost
        
        # update the heap
        #print verts
        #print verts.difference(X.intersection(verts))
        newVert = next(iter(verts.difference(X.intersection(verts))))
        X.add(newVert)
        #print len(X)
        
        for edge in adjList[newVert]:
            heapq.heappush(heap, (edge[1], set([edge[0], newVert])))
    return treeCost
    
        
    
def primMST(nodeNum, edges):
    V = set(range(1, nodeNum+1))
    X = set([1])
    
    tree = []
    
    while X != V:
        nextEdge = Edge(0,0,100000000)
        for edge in edges:
            if edge.v1 in X and edge.v2 not in X:
                if edge<nextEdge:
                    nextEdge = edge
            elif edge.v2 in X and edge.v1 not in X:
                if edge<nextEdge:
                    nextEdge = edge
        tree.append(nextEdge)
        if nextEdge.v1 in X:
            X.add(nextEdge.v2)
        else:
            X.add(nextEdge.v1)
            
    #print len(tree)
    cost = 0
    for edge in tree:
        cost = cost + edge.cost
    return cost
    #print X
        
        
    
    
    
    
if __name__ == "__main__":
    nodeNum, edges = readGraph('edges.txt')
    #print edges
    #print len(edges)
    print primHeap(nodeNum, edges)