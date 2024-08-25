#include <iostream>
#include <string>

using namespace std;

int main(){
    int N;
    cin >> N;
    for (int i = 0; i < N; i++){
        string cripto;
        int desloc;
        cin >> cripto;
        cin >> desloc;        
        string res;

        for (char letter : cripto){
            if ((letter - desloc) < 65){
                res += 91 - (desloc - (letter - 65));
            }else{
                res += letter - desloc;
            }
            
        }

        cout << res << endl;
    }
}