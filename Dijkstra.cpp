#include <iostream>
#define INF 999

using namespace std;

void output(int start, int dist[], int pred[])
{
    char outputnode[] ={'A','B','C','D','E','S'};
    for ( int x=0; x< 6; x++)
    {
        if ( x != start)
        {
            if( dist[x] != 999)
            {
                cout << "The distance of node " << outputnode[x] << " is " << dist[x] << endl;
                cout << outputnode[x];
                int j = x;
                do
                {
                    j = pred[j];
                    cout << " <- " << outputnode[j];
                }while(j != start);
                cout << endl;
            }
        }
    }
}

void dijkstra(int graph[6][6], int v, int start)
{
    int dist[INF], visited[INF], pred[INF], count, min_distance, nextnode = 0;
    
    for ( int x=0; x< 6; x++)
    {
        dist[x] = graph[start][x];
        pred[x] = start;
        visited[x] = 0;
    }
    
    dist[start] = 0;
    visited[start] = 1;
    count = 1;
    
    while(count < 6-1)
    {
        min_distance = INF;
        for ( int x=0; x< 6; x++)
        {
            if ( dist[x] < min_distance && !visited[x])
            {
                min_distance = dist[x];
                nextnode = x;
            }
        }
        
        visited[nextnode] = 1;
        
        for ( int x=0; x < 6; x++)
        {
            if ( !visited[x])
            {
                if ( (min_distance + graph[nextnode][x]) < dist[x])
                {
                    dist[x] =  min_distance + graph[nextnode][x];
                    pred[x] = nextnode;
                }
            }
        }
        dist[start] = 0;
        
        count++;
        
        
    }
    output(start, dist, pred);
}



int main()
{
    int src;
    int graph[6][6] = {
    {0,6,INF,INF,INF,INF},
    {INF,0,INF,1,2,INF},
    {4,INF,0,3,INF,INF},
    {INF,INF,INF,0,1,INF},
    {INF,INF,INF,INF,0,INF},
    {1,INF,2,INF,INF,0}
    };
    
    cout << "Enter source node: ";
    cin >> src;
    
    dijkstra(graph,6, src);
}


