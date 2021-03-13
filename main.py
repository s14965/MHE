import sys
import inputhandler
import utility

#nodes, edges = inputhandler.handlinginput(sys.argv)

def goalFunction(solution, edges):
    evaluations = []
    for s in solution:
        evaluations.append(utility.countConnections(s, edges))
    return sum(evaluations)/(len(nodes)*len(solution)*(len(solution)-1))

#example
nodes = [1, 2, 3, 4, 5, 6, 7]
edges = [
            [1, 2], [1, 3], [1, 4], [1, 5], [1, 6],
            [2, 3], [2, 4], [2, 5], [2, 7],
            [3, 4], [3, 5], [4, 5],
            [5, 6], [5, 7],
            [6, 7]
         ]

print(goalFunction([2,3,4,5], edges))
