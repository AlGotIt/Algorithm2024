#include <iostream>
#include <queue>

using namespace std;

int N, M;
int start_x, start_y;
int map[1001][1001];
int visited[1001][1001];
int dir[4][2] = {{-1,0}, {0,-1}, {1,0}, {0,1}}; //위, 좌, 하, 우

void bfs(int y, int x)
{
    queue<pair<int, int>> q;
    q.push(make_pair(y, x));

    while (!q.empty()) {
        int y = q.front().first;
        int x = q.front().second;
        q.pop();

        for (int i=0; i<4; i++) {
            int ny = y + dir[i][0];
            int nx = x + dir[i][1];

            if (ny < 0 || ny >= N || nx < 0 || nx >= M || (ny == start_y && nx == start_x)) continue;

            if (map[ny][nx] && !visited[ny][nx]) {
                q.push(make_pair(ny, nx));
                visited[ny][nx] = visited[y][x] + 1;
            }
        }
    }

}

int main()
{

    cin >> N >> M;
    
    for (int i=0; i<N; i++) {
        for (int j=0; j<M; j++) {
            int num;
            cin >> num;
            map[i][j] = num;
            if (num == 2) {
                start_y = i;
                start_x = j;
            }
        }
    }

    bfs(start_y, start_x);

    // 갈 수 있는 땅이지만 도달하지 못한경우
    for (int i=0; i<N; i++) {
        for (int j=0; j<M; j++) {
            if (map[i][j] && !visited[i][j]) {
                visited[i][j] = -1;
            }
        }
    }

    visited[start_y][start_x] = 0;

    for (int i=0; i<N; i++) {
        for (int j=0; j<M; j++) {
            cout << visited[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}