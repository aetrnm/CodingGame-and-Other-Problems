#include <iostream>
#include <string>
#include <map>
#include <queue>

using namespace std;

queue<int> q1;
queue<int> q2;

int card_p1;
int card_p2;

queue<int> cardsP1;
queue<int> cardsP2;

map<string, int> my_map = { { "2", 2 }, { "3", 3 }, { "4", 4 }, { "5", 5 }, { "6", 6 },
                            { "7", 7 }, { "8", 8 }, { "9", 9 }, { "10", 10 },
                            { "J", 11 }, { "Q", 12 }, { "K", 13 }, { "A", 14} };

int rounds_counter = 0;

void check_for_pat()
{
    if (q1.size() < 4 || q2.size() < 4)
    {
        cout << "PAT" << endl;
        exit(0);
    }
}

void compare_cards()
{
    card_p1 = q1.front();
    card_p2 = q2.front();

    // take the next significant pair of cards
    cardsP1.push(q1.front());
    cardsP2.push(q2.front());
    q1.pop();
    q2.pop();

    if (card_p1 > card_p2)
    {
        while (!cardsP1.empty())
        {
            q1.push(cardsP1.front());
            cardsP1.pop();
        }
        while (!cardsP2.empty())
        {
            q1.push(cardsP2.front());
            cardsP2.pop();
        }
    }
    else if (card_p2 > card_p1)
    {
        while (!cardsP1.empty())
        {
            q2.push(cardsP1.front());
            cardsP1.pop();
        }
        while (!cardsP2.empty())
        {
            q2.push(cardsP2.front());
            cardsP2.pop();
        }
    }
    else
    {
        check_for_pat();

        for (int i = 0; i < 3; i++) {
            cardsP1.push(q1.front());
            q1.pop();
        }
        for (int i = 0; i < 3; i++) {
            cardsP2.push(q2.front());
            q2.pop();
        }

        compare_cards();
    }
}

void print_winner()
{
    if (q1.empty())
    {
        cout << 2 << " " << rounds_counter;
    }
    else
    {
        cout << 1 << " " << rounds_counter;
    }
}

int main()
{
    int n;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        string s;
        cin >> s;
        s.erase(prev(s.end())); //deleting last character (card suit)
        q1.push(my_map.operator[](s));
    }

    int m;
    cin >> m;
    for (int i = 0; i < m; i++)
    {
        string s;
        cin >> s;
        s.erase(prev(s.end())); //deleting last character (card suit)
        q2.push(my_map.operator[](s));
    }

    while (!q1.empty() && !q2.empty())
    {
        compare_cards();
        rounds_counter++;
    }

    print_winner();
}
