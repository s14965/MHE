import utility
import itertools
from utility import isclique

def bruteforce(nodes, edges):
    '''
    Parameters
    ----------
    nodes : TYPE
        DESCRIPTION.
    edges : TYPE
        DESCRIPTION.

    Returns
    -------
    list of nodes that are in the biggest node
        
    Function checks every combination of nodes of every length. From the len(node) to 3.
    
    Example
    -------
    Input : ['x', 'y', 'z', 'w']
    Check if ['x', 'y', 'z', 'w'] is clique 
    if not
    then check if one of 
    ['x', 'y', 'z']
    ['x', 'y', 'w']
    ['x', 'z', 'w']
    ['y', 'z', 'w']
    is clique and so on.
    '''
    best_solution = []
    combs = []
    if utility.isclique(nodes, edges) == True:
        return nodes
    elif len(nodes)-1 > 2:
        for subset_len in range(len(nodes)-1, 2, -1):
            print("Looking in subsets of", subset_len)
            tmp = itertools.combinations(nodes, subset_len)                    
            for item in tmp:
                combs.append(list(item))
                
            for i, item in enumerate(combs):
                #print(i, item, isclique(item, edges))
                if utility.isclique(item, edges) & (len(item) > len(best_solution)):
                    return item
    print(best_solution, "of lenght", len(best_solution))
    return best_solution

if __name__ == '__main__':
    nodes =[1, 2, 3, 4, 5, 6, 7]
    edges = [[1,2],
          [1,3],[2,3],
          [1,4],[2,4],[3,4],
          [1,5],[2,5],[3,5],[4,5],
          [1,6],[5,6],
          [2,7],[5,7],[6,7]]
    
    print(bruteforce(nodes, edges))