#include <iostream>

using namespace std;

int main() {
    int N, CP, p;
    bool isW = true;
    cin >> N;
    cin >> CP;
    N--;
    while(N--){
        cin >> p;
        if(p > CP){
            isW = false;
            break;
        }
    }

    cout << (isW ? 'S' : 'N') << endl;
}
