import pandas as pd

def handlingInput(arg):
    if arg[0] == "-f":
        dataset = pd.read_csv('data/cliquedataset.csv') 

        edges = dataset.iloc[:, :190]
        nodes = dataset.iloc[:, 190:]
        
        print(edges)
        print(nodes)
        return nodes, edges