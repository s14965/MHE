import utility
import itertools
from utility import isclique

def bruteforce(nodes, edges):
   
    best_solution = []
    combs = []
    if utility.isclique(nodes, edges) == True:
        return nodes
    elif len(nodes)-1 > 2:
        for subset_len in range(len(nodes)-1, 2, -1):
            print("Looking in subsets of", subset_len)
            combs = itertools.combinations(nodes, subset_len)                    
            for item in combs:
                if utility.isclique(item, edges) & ( len(item) > len(best_solution) ):
                    return item
    return best_solution

if __name__ == '__main__':
    nodes =[1, 2, 3, 4, 5, 6, 7]
    edges = [
                [1, 2], [1, 3], [1, 4], [1, 5], [1, 6],
                [2, 3], [2, 4], [2, 5], [2, 7],
                [3, 4], [3, 5], [4, 5],
                [5, 6], [5, 7],
                [6, 7]
            ]
    print(bruteforce(nodes, edges))