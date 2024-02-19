#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N, M, H;
int town[11][11];
vector<pair<int,int>> vec_milk;
pair<int, int> home;

int result;

int find_milk(vector<int> v)
{
    int milk = 0;
    int power = M;
    int result = 0;
    pair<int, int> start = home;

    for (int& i : v) {
        pair<int, int> p = vec_milk[i-1];
        int y = p.first;
        int x = p.second;

        // 현재위치에서 갈 수 있는지 확인
        int distance = abs(start.first - y) + abs(start.second - x);
        if (distance <= power) {
            milk++;
            power = power - distance + H;
            start = p; // 현재위치 변경

            // 집으로 돌아갈 수 있을 때
            if ((abs(home.first - y) + abs(home.second - x)) <= power) {
                result = milk;
            }
        } else {
            break;
        }
    }

    return result;
}

int main()
{
    cin >> N >> M >> H;

    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            cin >> town[i][j];
            if (town[i][j] == 1) {
                home = make_pair(i, j);
            } else if (town[i][j] == 2) {
                vec_milk.push_back(make_pair(i, j));
            }
        }
    }

    // vec_milk 순열 생성 후 find_milk
    int cnt_milk = vec_milk.size();
    vector<int> vec_perm;
    for (int i=1; i<=cnt_milk; i++) {
        vec_perm.push_back(i);
    }

    do {
        result = max(result, find_milk(vec_perm));
    } while(next_permutation(vec_perm.begin(), vec_perm.end()));

    cout << result << endl;

    return 0;
}