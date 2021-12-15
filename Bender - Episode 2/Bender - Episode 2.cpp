#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

struct Room
{
    int amountOfMoney = 0;
    int firstNeighbourRoom = 0;
    int secondNeighbourRoom = 0;
    int bestPassToThis = 0;

    Room(int money, string fNR, string sNR)
    {
        amountOfMoney = money;
        if (fNR == "E")
        {
            firstNeighbourRoom = -1;
        }
        else 
        {
            firstNeighbourRoom = stoi(fNR);
        }
        if (sNR == "E")
        {
            secondNeighbourRoom = -1;
        }
        else
        {
            secondNeighbourRoom = stoi(sNR);
        }
    }
};

int exitBestSum = 0;

Room* rooms[10000];

bool CheckPath(Room* room, int neighbourIndex)
{
    if (neighbourIndex != -1)
    {
        Room* neighbour = rooms[neighbourIndex];
        int expectedNewPass = room->bestPassToThis + neighbour->amountOfMoney;
        if (neighbour->bestPassToThis < expectedNewPass)
        {
            neighbour->bestPassToThis = expectedNewPass;
            return true;
        }
    }
    else
    {
        if (exitBestSum < room->bestPassToThis)
        {
            exitBestSum = room->bestPassToThis;
        }
    }
    return false;
}

void EnterRoom(Room* room)
{
    bool possibleFirstRoom = CheckPath(room, room->firstNeighbourRoom);
    bool possibleSecondRoom = CheckPath(room, room->secondNeighbourRoom);
    if (possibleFirstRoom) {
        EnterRoom(rooms[room->firstNeighbourRoom]);
    }
    if (possibleSecondRoom) {
        EnterRoom(rooms[room->secondNeighbourRoom]);
    }
}

int main()
{
    int N;
    cin >> N; cin.ignore();
    for (int i = 0; i < N; i++) {
        int index;
        int inputMoney;
        string firstNeighbourRoom;
        string secondNeighbourRoom;
        cin >> index >> inputMoney >> firstNeighbourRoom >> secondNeighbourRoom;
        rooms[index] = new Room(inputMoney, firstNeighbourRoom, secondNeighbourRoom);
    }
    rooms[0]->bestPassToThis = rooms[0]->amountOfMoney;

    EnterRoom(rooms[0]);

    cout << exitBestSum << endl;
}