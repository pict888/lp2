#include <iostream>
#include <algorithm>
using namespace std;

struct Job
{
    int id;
    int deadline;
    int profit;
};

bool compare(Job a, Job b)
{
    return a.profit > b.profit;
}

int main()
{
    int n;
    bool slot[100] = {false};
    int totalProfit = 0;
    cout << "Enter number of jobs: ";
    cin >> n;
    Job jobs[100];

    cout << "Enter deadline and profit:\n";

    for (int i = 0; i < n; i++)
    {
        jobs[i].id = i + 1;

        cin >> jobs[i].deadline >> jobs[i].profit;
    }

    // Sort by maximum profit
    sort(jobs, jobs + n, compare);

    cout << "\nSelected Jobs:\n";

    for (int i = 0; i < n; i++)
    {
        // Check slot backward
        for (int j = jobs[i].deadline - 1; j >= 0; j--)
        {
            if (slot[j] == false)
            {
                slot[j] = true;
                totalProfit += jobs[i].profit;
                cout << "Job "<< jobs[i].id << endl;
                break;
            }
        }
    }

    cout << "Total Profit = " << totalProfit;
}