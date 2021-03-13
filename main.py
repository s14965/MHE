import sys
import inputhandler
import utility
import bruteforce

nodes, edges = inputhandler.handlingInput(sys.argv)

def goalFunction(solution, edges):
    evaluations = []
    for s in solution:
        evaluations.append(utility.countConnections(s, edges))
            
    if utility.isclique(solution, edges):
        penalty = 0
    else:
        penalty = -1
    
    return penalty + sum(evaluations) / ( len(nodes) 
                                         * ( len(nodes) - len(solution) ) 
                                         * ( len(solution)  - 1 ) )

print(goalFunction([6,7,4,5], edges))
print(goalFunction([2,3,4,5], edges))
print(goalFunction([2,3,4,6], edges))
print(goalFunction([2,3,4,7], edges))
print(goalFunction([1,2,3,4,5], edges))

print(bruteforce.bruteforce(nodes, edges))