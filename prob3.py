from dijkstra import assignInfinity
from dijkstra import process
from dijkstra import outputshortestdistance

graph = {
    'a': {'b':3,'c':5,'d':9},
    'b': {'a':3,'c':3,'d':4,'e':7},
    'c': {'a':5,'b':3,'d':2,'e':6,'f':8},
    'd': {'b':4,'c':2,'e':2,'f':2,'a':9},
    'e': {'b':7,'c':6,'d':2,'f':5},
    'f':{'d':2,'e':5,'c':8},
}

#input and output
print("Enter starting node: ")
start = input()
print("Enter ending node: ")
end = input()

assignInfinity(graph,start,end)
process(graph,start,end)
outputshortestdistance(graph,start,end)