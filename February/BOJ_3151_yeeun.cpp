#include <iostream>
#include <vector>
#include <algorithm>

using namespace std; 

int N;
vector<int> code_lv;
long long res;

// 이진 탐색 : 특정 값의 첫 번째 등장 위치를 찾는 함수
int lower_bound(const vector<int>& vec, int start, int target) {
    int left = start;
    int right = vec.size();

    while (left < right) {
        int mid = left + (right - left) / 2;
        if (vec[mid] < target) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }

    return left;
}

// 이진 탐색 : 특정 값의 마지막 등장 위치를 찾는 함수
int upper_bound(const vector<int>& vec, int start, int target) {
    int left = start;
    int right = vec.size();

    while (left < right) {
        int mid = left + (right - left) / 2;
        if (vec[mid] <= target) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }

    return left;
}

int main()
{
    cin >> N;

    for (int i=0; i<N; i++) {
        int num = 0;
        cin >> num;

        code_lv.push_back(num);
    }

    sort(code_lv.begin(), code_lv.end());

    for (int i = 0; i < N - 2; i++) {
        for (int j = i + 1; j < N - 1; j++) {
            int sum = code_lv[i] + code_lv[j];

            // 벡터 내 -sum 개수
            res += upper_bound(code_lv, j+1, -sum) - lower_bound(code_lv, j+1, -sum);
            /*
                c++ 제공 라이브러리를 사용할 수도 있다
                res += upper_bound(code_lv.begin()+j+1, code_lv.end(), -sum) - lower_bound(code_lv.begin()+j+1, code_lv.end(), -sum);
            */
        }
    }

    cout << res << endl;

    return 0;
}