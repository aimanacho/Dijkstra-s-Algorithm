from dijkstra import assignInfinity
from dijkstra import process
from dijkstra import outputshortestdistance

graph = {
    'a': {'b':4,'c':2},
    'b': {'c':5,'d':10},
    'c': {'e':3},
    'd': {'f':11},
    'e': {'d':4},
    'f': {},
}

#input and output
print("Enter starting node: ")
start = input()
print("Enter ending node: ")
end = input()

assignInfinity(graph,start,end)
process(graph,start,end)
outputshortestdistance(graph,start,end)