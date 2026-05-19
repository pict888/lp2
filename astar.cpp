#include <iostream>
#include <vector>
#include <queue>

using namespace std;

vector<int> goal(9);

// State
struct State {

    vector<int> board;

    int g, h, f;

    int blank;
};

// Min Heap Compare
struct Compare {

    bool operator()(State a, State b) {

        return a.f > b.f;
    }
};

// Find Blank Position
int findBlank(vector<int> b) {

    for(int i = 0; i < 9; i++) {
        if(b[i] == -1)
            return i;
    }

    return -1;
}

// Simple Heuristic
// Count misplaced tiles
int heuristic(vector<int> b) {

    int count = 0;

    for(int i = 0; i < 9; i++) {

        if(b[i] != -1 && b[i] != goal[i]) {
            count++;
        }
    }

    return count;
}

// Print Board
void printBoard(vector<int> b) {

    for(int i = 0; i < 9; i++) {

        if(b[i] == -1)
            cout << "_ ";
        else
            cout << b[i] << " ";

        if(i % 3 == 2)
            cout << endl;
    }
}

// A* Algorithm
void Astar(vector<int> start) {

    priority_queue<State,vector<State>,Compare> pq;

    State s;
    s.board = start;
    s.blank = findBlank(start);
    s.g = 0;
    s.h = heuristic(start);
    s.f = s.g + s.h;

    pq.push(s);
    while(!pq.empty()) {
        State cur = pq.top();
        pq.pop();

        // Goal Found
        if(cur.board == goal) {
            cout << "\nGoal State Found:\n";
            printBoard(cur.board);
            return;
        }
        
        int b = cur.blank;
        int dr[4] = {-1, 1, 0, 0};
        int dc[4] = {0, 0, -1, 1};
        // Generate Children
        for(int i = 0; i < 4; i++) {
            int nr = b/3 + dr[i];
            int nc = b%3 + dc[i];
            // Valid Move
            if(nr >= 0 && nr < 3 && nc >= 0 && nc < 3) {
                int ni = nr*3 + nc;
                State child = cur;
                swap(child.board[b],child.board[ni]);
                child.blank = ni;
                child.g = cur.g + 1;
                child.h = heuristic(child.board);
                child.f = child.g + child.h;
                pq.push(child);
            }
        }
    }

    cout << "No Solution";
}

// Main
int main() {

    vector<int> start(9);

    cout << "Enter Initial Board:\n";

    for(int i = 0; i < 9; i++)
        cin >> start[i];

    cout << "Enter Goal Board:\n";

    for(int i = 0; i < 9; i++)
        cin >> goal[i];

    Astar(start);

    return 0;
}
/*
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

vector<int> goal(9);

// State
struct State
{

    vector<int> board;

    int g, h, f;

    int blank;

    State *parent;
};

// Min Heap
struct Compare
{

    bool operator()(State *a, State *b)
    {

        return a->f > b->f;
    }
};

// Find blank
int findBlank(vector<int> b)
{

    for (int i = 0; i < 9; i++)
    {

        if (b[i] == -1)
            return i;
    }

    return -1;
}

// Manhattan Distance
int manhattan(vector<int> b)
{

    int dist = 0;

    for (int i = 0; i < 9; i++)
    {

        if (b[i] == -1)
            continue;

        for (int j = 0; j < 9; j++)
        {

            if (goal[j] == b[i])
            {

                dist += abs(i / 3 - j / 3) + abs(i % 3 - j % 3);
            }
        }
    }

    return dist;
}

// Print board
void printBoard(vector<int> b)
{

    for (int i = 0; i < 9; i++)
    {

        if (b[i] == -1)
            cout << "_ ";
        else
            cout << b[i] << " ";

        if (i % 3 == 2)
            cout << endl;
    }
}

// Print steps
void printPath(State *s)
{

    vector<State *> path;

    while (s != nullptr)
    {

        path.push_back(s);

        s = s->parent;
    }

    reverse(path.begin(), path.end());

    cout << "\nFinal Solution:\n";

    for (int i = 0; i < path.size(); i++)
    {

        cout << "\nStep " << i << ":\n";

        printBoard(path[i]->board);
    }
}

// Generate children
vector<State *> children(State *cur)
{

    vector<State *> childs;

    int b = cur->blank;

    int dr[4] = {-1, 1, 0, 0};
    int dc[4] = {0, 0, -1, 1};

    for (int i = 0; i < 4; i++)
    {

        int nr = b / 3 + dr[i];
        int nc = b % 3 + dc[i];

        if (nr >= 0 && nr < 3 &&
            nc >= 0 && nc < 3)
        {

            int ni = nr * 3 + nc;

            State *ch = new State;

            ch->board = cur->board;

            swap(ch->board[b],
                 ch->board[ni]);

            ch->blank = ni;

            ch->g = cur->g + 1;

            ch->h = manhattan(ch->board);

            ch->f = ch->g + ch->h;

            ch->parent = cur;

            childs.push_back(ch);
        }
    }

    return childs;
}

// A* Search
void Astar(vector<int> start)
{

    priority_queue<State *,
                   vector<State *>,
                   Compare>
        open;

    vector<vector<int>> closed;

    State *startState = new State;

    startState->board = start;

    startState->blank = findBlank(start);

    startState->g = 0;

    startState->h = manhattan(start);

    startState->f = startState->h;

    startState->parent = nullptr;

    open.push(startState);

    while (!open.empty())
    {

        State *cur = open.top();

        open.pop();

        if (cur->board == goal)
        {

            printPath(cur);

            return;
        }

        closed.push_back(cur->board);

        vector<State *> childs =
            children(cur);

        for (State *ch : childs)
        {

            if (find(closed.begin(),
                     closed.end(),
                     ch->board) == closed.end())
            {

                open.push(ch);
            }
        }
    }

    cout << "No Solution";
}

// Main
int main()
{

    vector<int> start(9);

    cout << "Enter Initial Board:\n";

    for (int i = 0; i < 9; i++)
        cin >> start[i];

    cout << "Enter Goal Board:\n";

    for (int i = 0; i < 9; i++)
        cin >> goal[i];

    Astar(start);

    return 0;
}
*/
