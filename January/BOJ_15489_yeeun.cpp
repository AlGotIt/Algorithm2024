#include <iostream>

using namespace std;

int dp[31][31];

int main()
{
    int R, C, W;

    cin >> R >> C >> W;

    for (int i = 1; i < 31; i++) {
        dp[i][0] = 1;
    }

    for (int i = 3; i < 31; i++) {
        for (int j = 1; j <= i / 2; j++) {
            if (j == i/2 && i%2 == 0) continue;
            dp[i][j] = (dp[i-1][j] ?: dp[i-1][j-1]) + dp[i-1][j-1];
        }
    }

    int res = 0;
    for (int i = 1; i <= W; i++) {
        for (int j = 0; j < i; j++) {
            int num = dp[R+i-1][C+j-1] ?: dp[R+i-1][(R+i-1) - (C+j-1) - 1];
            res += num;
        }
    }

    cout << res;

    return 0;
}