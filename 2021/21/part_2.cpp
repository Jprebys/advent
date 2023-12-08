#include <cstdio>

struct Player
{
    int pos;
    int score;
};

void move(Player *p, int move)
{
    p->pos = ((p->pos - 1 + move) % 10) + 1;
    p->score += p->pos;
}

void turn(Player *p, int &dice)
{
    int roll = 0;
    for (int i = 0; i < 3; ++i) {
        roll += dice;
        ++dice;
        if (dice > 100)
            dice = 1;
    }
    move(p, roll);
}

int main()
{
    Player p1 = {3, 0};
    Player p2 = {10, 0};
    Player *players[] = {&p1, &p2};
    int dice = 1;

    int i = 0;
    Player *p = players[i];
    do {
        p = players[i];
        turn(p, dice);
        i = (i + 1) & 1;
    } while (p->score < 1000);

    Player *loser = players[0]->score < players[1]->score ? players[0] : players[1];

    printf("%d %d\n", players[0]->score, players[1]->score);
    printf("%d\n", loser->score);
    return 0;
}