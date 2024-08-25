#include <string>
#include <iostream>
#include <sstream>
#include <limits>
#include <cmath>
using namespace std;
int main(){
    int N;
    cin >> N;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');
    string texto;
    while(getline(cin, texto)){
        string res;

        // Pode ocorrer erro aqui dependendo de onde estiver executando o codigo
        // O padrão atual será executado SEM ERRO no beecrowd, pórem caso execução local, será necessário trocar para -2
        int ss = texto.length() - 1;

        int meio = floor((float) ss / 2);
        for (int i = meio; i >= 0; i--) {
            res += texto[i];
        }
        for (int i = ss; i > meio; i--) {
            res += texto[i];
        }
        cout << res << endl;
    }
    return 0;

}
