#include <iostream>
#include <vector>

using namespace std;

int N, M, H;
int result;
int visited[11][11];
pair<int, int> home;
vector<pair<int,int>> vec_milk;

void dfs(pair<int, int> p, int h, int m) // 현재 좌표, 남은 체력, 마신 우유
{
    // 집으로 돌아갈 수 있다면 최대우유 개수 갱신
    if ((abs(p.first - home.first) + abs(p.second - home.second)) <= h) {
        result = max(result, m);
    }

    visited[p.first][p.second] = 1;

    for (pair<int, int>& v : vec_milk) {
        int ny = v.first;
        int nx = v.second;
        int distance = abs(ny-p.first) + abs(nx-p.second);

        // 방문하지 않았고, 남은체력으로 이동가능한 경우
        if (!visited[ny][nx] && (distance <= h)) {
            int next_h = h - distance + H;
            int next_m = m + 1;

            dfs(v, next_h, next_m);

            visited[ny][nx] = 0; // 방문 초기화    
        }
    }

}


int main()
{
    cin >> N >> M >> H;

    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            int n;
            cin >> n;
            if (n == 1) {
                home = make_pair(i, j);
            } else if (n == 2) {
                vec_milk.push_back(make_pair(i, j));
            }
        }
    }

    dfs(home, M, 0);

    cout << result << endl;

    return 0;
}