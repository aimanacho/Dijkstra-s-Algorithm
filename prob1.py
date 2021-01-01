from dijkstra import assignInfinity
from dijkstra import process
from dijkstra import outputshortestdistance

graph = {
    's': {'a':1, 'c':2},
    'a': {'b':6},
    'b': {'e':2, 'd':1},
    'c': {'a':4, 'd':3},
    'd': {'e':1},
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