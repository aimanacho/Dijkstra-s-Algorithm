from math import inf

#declaration 
#graph is considered as unvisited
visited = [] # 
shortest_distance = {} # take the shortest node to reach destination
tracking = {} #searching for the optimal route
path_tracking = [] # path to the route (prev_node)

def assignInfinity(graph,start,end):
    #assign all nodes of shortest distance to inf except starting node
    for node in graph:
        shortest_distance[node] = inf
    shortest_distance[start] = 0


def process(graph,start,end):
    while graph:
        min_distance = None
        #check the index for the smallest distance of node 
        for node in graph:
            if min_distance is None:
                min_distance = node
            elif shortest_distance[node] < shortest_distance[min_distance]:
                min_distance = node
    
        path_options = graph[min_distance].items()

        tracking[start] = 0

        for child_node, weight in path_options:
            calc_distance = weight + shortest_distance[min_distance]
            if calc_distance < shortest_distance[child_node]:
                shortest_distance[child_node] = calc_distance
                tracking[child_node]= min_distance

        graph.pop(min_distance)
        visited.append(min_distance) 

def outputshortestdistance(graph,start,end):
    curNode = end
    while curNode != start:
        try:
            path_tracking.insert(0, curNode)
            curNode = tracking[curNode]
        except:
            print("Path does not exist")
            break
        
    path_tracking.insert(0, start)
    
    if shortest_distance[end] != inf:
        print("\nShortest distance is " + str(shortest_distance[end]))
        print("Path = " + str(path_tracking))
        print("\n------------------------------------Table------------------------------------------")
        print("Vertex\t|\tShortest distance from vertex " + start.upper() + "\t|\t Previous vertex")
        for node in tracking:
            print(str(node) + "\t\t" + str(shortest_distance[node])+ "\t\t\t\t\t\t" + str(tracking[node]))
    
    
