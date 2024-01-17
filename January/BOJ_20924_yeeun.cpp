#include <iostream>
#include <vector>

using namespace std;

typedef vector<vector<pair<int, int>>> vec;

int N, R;
int visited[200001];
int giga_node, gi_len, ga_len;

void dfs(const vec& v, int n, int len)
{
    if (visited[n]) return;

    visited[n] = 1;

    // 기가노드를 만난 경우
    if (giga_node == 0 && v[n].size() > 2) {
        giga_node = n;
        gi_len = len;
        len = 0;
    }

    // 리프노드를 만난 경우
    if (v[n].size() == 1) {
        ga_len = max(ga_len, len);
    }

    for (const auto& edge : v[n]) {
        int next_node = edge.first;
        int weight = edge.second;

        dfs(v, next_node, len+weight);
    }
}

int main ()
{
    cin >> N >> R;

    vec grph(N+1);

    for (int i=0; i<N-1; i++) {
        int a, b, d;
        cin >> a >> b >> d;

        grph[a].push_back(make_pair(b, d));
        grph[b].push_back(make_pair(a, d));
    }

    if (grph[R].size() > 1) { // 루트노드 == 기가노드인 경우
        giga_node = R;
    }

    dfs(grph, R, 0);
    
    if (giga_node == 0) { // 기가노드 == 리프노드인 경우
        gi_len = ga_len;
        ga_len = 0;
    }

   cout << gi_len << " " << ga_len;

    return 0;
}
