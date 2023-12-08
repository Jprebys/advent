#include <cstdio>
#include <fstream>
#include <iostream>
#include <string>


void fix_values(int &min, int &max)
{
    if (min < -50) min = -50;
    if (max > 50) max = 50;

    min += 50;
    max += 50;
}


int main()
{

    int board[101][101][101] = {0};

    std::ifstream file("2/input.txt");

    std::string line;

    int minx, maxx, miny, maxy, minz, maxz;
    std::string fmt;
    int val;
    int total = 0;
    while (std::getline(file, line)) {

        if (line[1] == 'n') {
            fmt = "on x=%d..%d,y=%d..%d,z=%d..%d\n";
            val = 1;
        } else {
            fmt = "off x=%d..%d,y=%d..%d,z=%d..%d\n";
            val = 0;
        }
        int rc = sscanf(line.c_str(), fmt.c_str(), &minx, &maxx, &miny, &maxy, &minz, &maxz);
        if (rc != 6) {
            printf("error num of args\n");
            return 1;
        }
        fix_values(minx, maxx);
        fix_values(miny, maxy);
        fix_values(minz, maxz);

        std::cout << minx << maxx << miny << maxy << minz << maxz << '\n';

        for (int x = minx; x <= maxx; x++) {
            for (int y = miny; y <= maxy; y++) {
                for (int z = minz; z <= maxz; z++) {
                    if (!board[x][y][z] && val) {
                        total++;
                    } else if (board[x][y][z] && !val) {
                        total--;
                    }
                    board[x][y][z] = val;
                }
            }
        }
    }

    printf("%d\n", total);
    return 0;
}