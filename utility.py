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