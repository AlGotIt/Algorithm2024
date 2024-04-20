#include <iostream>
#include <set>

using namespace std;

int N, M, balance;
int fee[10001];
int unf[10001];

int find(int n)
{
    if (unf[n] == n) {
        return n;
    } else {
        return find(unf[n]);
    }
}

void set_union(int a, int b)
{
    int root_a = find(a);
    int root_b = find(b);

    unf[root_a] = root_b;
}

int main()
{
    cin >> N >> M >> balance;

    int num;
    for (int i=1; i<=N; i++) {
        cin >> num;
        fee[i] = num;
        unf[i] = i; // union_find 초기 세팅 (부모노드는 자기 자신)
    }

    int f1, f2;
    for (int i=1; i<=M; i++) {
        cin >> f1 >> f2;
        set_union(f1, f2); // 서로소집합 세팅
    }

    int arr_root[N+1]; // 해당 집합군에서 최소 비용을 저장
    set<int> set_root;
    fill_n(arr_root, N+1, 10000);

    // 각 루트별 최소 비용
    for (int i=1; i<=N; i++) {
        int root_i = find(i);
        // cout << "node " << i << ", root: " << find(i) << ", fee: " << fee[i] << ", ar[ri]: " << arr_root[root_i] << endl;
        
        arr_root[root_i] = min(fee[i], arr_root[root_i]);
        set_root.insert(root_i);
    }

    int need_money = 0;
    for (auto i : set_root) {
        // cout << "root " << i << ", 최소비용: " << arr_root[i] << endl;
        need_money += arr_root[i];
    }

    if (balance >= need_money) {
        cout << need_money << endl;
    } else {
        cout << "Oh no" << endl;
    }

    return 0;
}