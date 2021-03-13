import sys
import inputhandler
import utility
import bruteforce

input_nodes, input_edges = inputhandler.handlingInput(sys.argv)

def goalFunction(solution, nodes, edges):
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

print("from input")
print(goalFunction([6,7,4,5], input_nodes, input_edges))
print(goalFunction([2,3,4,6], input_nodes, input_edges))
print(goalFunction([2,3,4,7], input_nodes, input_edges))
print(goalFunction([2,3,4,5], input_nodes, input_edges))
solution = bruteforce.bruteforce(input_nodes, input_edges)
print(goalFunction(solution, input_nodes, input_edges))
print(solution)

print()
print("from rand")
nodes2, edges2 = utility.generateGraph(graphSize = 20)
rand_solution = utility.randSolution(nodes2)
print(rand_solution)
print(goalFunction(rand_solution, nodes2, edges2))
brut_solution = bruteforce.bruteforce(nodes2, edges2)
print(goalFunction(brut_solution, nodes2, edges2))
print(brut_solution)
