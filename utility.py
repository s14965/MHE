def countConnections(node, edges):
    con = 0
    for i in edges:
        if node in i:
            con += 1
    return con

