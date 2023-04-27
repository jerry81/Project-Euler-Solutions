/*

It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?

99 1
98 2
97 3

2 -> 1 1  (1)
3 -> 1 2, 1 1 1     1, (2)      1, 2  (2)
4 -> 1,1,1,1   2,1,1   3,1   2,2  (4)     1, (3)  1, 3
5 -> 1, (4)   2, (3) -> 2   3 (2) -> 1  4,1
4+2
1,



*/
#include <unordered_map>
#include <iostream>

bool visited[101];
int counts[101];

using namespace std;
int main() {
  visited[2] = true;
  counts[2] = 1;
  int cur = counts[2];
  for (int i = 3; i < 8; ++i) {
    for (int i = 2, i < )
    counts[i] = counts[i-1] + 1;
  }
  return 0;
}