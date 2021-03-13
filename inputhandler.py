import sys
import pandas as pd

def str_to_int_list(argv):
    int_list = []
    argv = argv.split(',')
    
    for a in argv:
        int_list.append(int(a))
    return int_list
    

def handlingInput(argv):
    #if argv[1] == "-f" or "-F" or "--File":
    file = open(argv[1])
    n = file.readline()
    e = file.readline()
        
    nodes = str_to_int_list(n)
    e = e.split(';')
    edges = []
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
    