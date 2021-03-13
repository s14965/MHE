import random

def countConnections(node, edges):
    con = 0
    for i in edges:
        if node in i:
            con += 1
    return con

def isclique(solution, edges):
    for node in solution:
        solution2 = solution [solution.index(node) + 1:]
        for nextNode in solution2:
            if [node, nextNode] in edges or [nextNode, node] in edges:         #sprawdza w tablicy globalnej
                continue
            else:
              return False     
    return True

def randSolution(nodes):
    size = random.randint(3, len(nodes))
    
    solution = []
    i=0
    while(i < size):
        choice = random.choice(nodes)
        if choice not in solution:
            solution.append(choice)
            i += 1
    return solution

def shuffle(nodes):
    tmp = nodes.copy()
    tmp2 = []
    for i in range(len(nodes)):
        rand = random.choice(tmp)
        tmp2.append(rand)
        tmp.pop(tmp.index(rand))
    return tmp2

def generateGraph(graphSize = 20, edgeRate = 0.7):
    nodes=[]
    edges=[]
    i=0
    while i < graphSize:
        i+=1
        nodes.append(i)
    nodes = shuffle(nodes)
    for node in nodes:
        tmp = []
        edgeCount = random.randint(2, graphSize * edgeRate)                           # losowanie ilosci krawedzi dla wezla
        for i in range(0, edgeCount):
            if len(set(nodes) - set(tmp)) > 0:
                tmp.append(random.choice(list(set(nodes)-set(tmp)-set([node]))))            # jesli zadna krawedz nie laczy sie z clique'a, to wylosowac jeden z wezlow clique'i dla ostatniej krawedzi
        for n in tmp:
            edge = [node, n]
            edge.sort()
            if edge not in edges:
                edges.append(edge)
                edges.sort()
        del tmp    
    return [nodes, edges]