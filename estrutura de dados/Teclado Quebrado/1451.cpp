#include <iostream>
#include <string>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    string texto;
    while (cin >> texto){

        string s;
        int pos = 0;
        for (char letter : texto){
            if (letter == '[') pos = 0;
            else if (letter == ']') pos = s.size();
            else {
                s.insert(pos++, 1, letter);
            }
        }

        cout << s << endl;
        
    }
    return 0;
}