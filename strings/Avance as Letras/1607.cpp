#include <iostream>
#include <string>

using namespace std;

int letter_to_letter(char atual, char alvo){
    if(alvo - atual < 0){
        return ('z' - atual) + 1 + (alvo - 'a'); 
    }
    return alvo - atual;
}
int main(){

    int N, ts;
    string atual, alvo;
    cin >> N;
    for (int i = 0; i < N; i++){
        cin >> atual >> alvo;
        ts = atual.length();
        int res = 0;
        for (int j = 0; j < ts; j++){
            res += letter_to_letter(atual[j], alvo[j]);
        }

        cout << res << endl;
    }
    return 0;
}