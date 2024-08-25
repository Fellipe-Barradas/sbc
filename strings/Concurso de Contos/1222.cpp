#include <string>
#include <iostream>
#include <sstream>
#include<iostream>
#include<limits>
using namespace std;

int main(){
    int N, L, C;
    int paginas, linhas, caracteres;
    string palavra;
    while (cin >> N >> L >> C){
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
        paginas = linhas = caracteres = 0;
        getline(cin, palavra);
        palavra.pop_back();
        istringstream iss(palavra);
        string word;
        while (iss >> word){
            int ps = word.length(); 
            if (ps + caracteres < C){
                caracteres += ps + 1;
            } else if(ps + caracteres == C){
                caracteres=0; 
                linhas++;
            } else {
                linhas++;
                caracteres=0;
                caracteres+=ps+1;
            }

            if (linhas == L){
                paginas++;
                linhas = 0; 
            }
        }

        if (linhas > 0 || caracteres > 0){
            paginas++;
        }

        cout << paginas << endl;
    }
    return 0;
}
