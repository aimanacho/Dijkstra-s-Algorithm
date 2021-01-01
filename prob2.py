from dijkstra import assignInfinity
from dijkstra import process
from dijkstra import outputshortestdistance

graph = {
    'a': {'e':7},
    'b': {'a':4},
    'c': {'b':1},
    'd': {'b':2, 'c':6},
    'e': {},
}

#input and output
print("Enter starting node: ")
start = input()
print("Enter ending node: ")
end = input()

assignInfinity(graph,start,end)
process(graph,start,end)
outputshortestdistance(graph,start,end)