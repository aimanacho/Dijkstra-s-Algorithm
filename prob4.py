from dijkstra import assignInfinity
from dijkstra import process
from dijkstra import outputshortestdistance

graph = {
    'a': {'b':3,'c':5},
    'b': {'c':2,'d':6},
    'c': {'b':1,'d':4,'f':6},
    'd': {'f':2},
    'f':{'a':3,'d':7},
}

#input and output
print("Enter starting node: ")
start = input()
print("Enter ending node: ")
end = input()

assignInfinity(graph,start,end)
process(graph,start,end)
outputshortestdistance(graph,start,end)