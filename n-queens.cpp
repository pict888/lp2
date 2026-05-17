#include <iostream>
#include <vector>

using namespace std;

int n;
bool found = false;

vector<int> board;

// Check if safe
bool isSafe(int row, int col) {

    for(int i = 0; i < row; i++) {

        // Same column
        if(board[i] == col)
            return false;

        // Diagonal
        if(abs(board[i] - col) == abs(i - row))
            return false;
    }

    return true;
}

// Print board
void printBoard() {

    cout << "\nSolution:\n\n";

    for(int i = 0; i < n; i++) {

        for(int j = 0; j < n; j++) {

            if(board[i] == j)
                cout << " Q ";
            else
                cout << " . ";
        }

        cout << endl;
    }
}

// Backtracking
void solve(int row) {

    // Stop after first solution
    if(found)
        return;

    // Base case
    if(row == n) {

        found = true;
        printBoard();
        return;
    }

    // Try all columns
    for(int col = 0; col < n; col++) {

        if(isSafe(row, col)) {

            // Place queen
            board[row] = col;

            // Recurse
            solve(row + 1);

            // Backtrack
            board[row] = -1;
        }
    }
}

int main() {

    cout << "Enter number of queens: ";
    cin >> n;

    board.resize(n, -1);

    solve(0);

    if(!found)
        cout << "\nNo solution exists";

    return 0;
}
