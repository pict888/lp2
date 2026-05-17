#include <iostream>
#include <climits>
using namespace std;

int main()
{
    int n;

    cout << "Enter number of nodes: ";
    cin >> n;

    int graph[10][10];

    cout << "Enter adjacency matrix:\n";

    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        {
            cin >> graph[i][j];
        }
    }

    int source;

    cout << "Enter source node: ";
    cin >> source;

    int dist[10];
    bool visited[10];

    // Initialize
    for(int i=0;i<n;i++)
    {
        dist[i] = INT_MAX;
        visited[i] = false;
    }

    dist[source] = 0;

    // Dijkstra Algorithm
for(int i=0;i<n-1;i++)
{
    int u;
    int min = INT_MAX;

    // Find nearest node
    for(int j=0;j<n;j++)
    {
        if(visited[j] == false && dist[j] < min)
        {
            min = dist[j];
            u = j;
        }
    }

    visited[u] = true;

    // Update neighbors
    for(int v=0;v<n;v++)
    {
        if(graph[u][v] != 0)
        {
            int newDist = dist[u] + graph[u][v];

            if(newDist < dist[v])
            {
                dist[v] = newDist;
            }
        }
    }
}

    cout << "\nShortest Distances:\n";

    for(int i=0;i<n;i++)
    {
        cout << source << " -> " << i << " = " << dist[i] << endl;
    }

    return 0;
}