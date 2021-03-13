import sys
import pandas as pd

def handlingInput(argv):
    file = open(argv[1])
    n = file.readline()
    e = file.readline()
        
    nodes = []
    n = n.split(',')
    for a in n:
        nodes.append(int(a))
    
    edges = []
    e = e.split(';')
    for i in e:
        i = i.split(',')
        tmp = [ int( i[0] ), int( i[1] ) ]
        tmp.sort()
        edges.append(tmp)
        
    # print("node len: ", len(nodes))    
    # print(nodes)
    # print("edge len: ", len(edges))    
    # print(edges)
    return nodes, edges
    
if __name__ == '__main__':
    handlingInput(sys.argv)
    