#include <iostream>
#include <vector>
#include <string>
#include <set>
 
using namespace std;
 
string arr_alpha[1000];
 
int main()
{
    int R, C;
    vector<string> vec_alpha;
 
    cin >> R >> C;
 
    for(int i=0; i<R; i++) {
        cin >> arr_alpha[i];
    }
 
    for (int i=0; i<C; i++) {
        string str = "";
        for (int j=0; j<R; j++) {
            str += arr_alpha[j][i];
        }
        vec_alpha.push_back(str);
    }
 
    int cnt;
    for (cnt=0; cnt<R-1; cnt++) {
        for (string& s : vec_alpha) {
            s = s.substr(1);
        }
        
        set<string> s(vec_alpha.begin(), vec_alpha.end());
        if (s.size() != C) {
            break;
        }
    }
 
    cout << cnt << endl;
 
    return 0;
}
 