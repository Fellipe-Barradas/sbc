#include <string>
#include <iostream>
#include <unordered_set>
#include <cctype>

using namespace std;

int main(){
    int N;
    scanf("%d\n", &N);
    for (int i = 0; i < N; i++){
        string text;
        unordered_set<char> letters;
        getline(cin, text);
        int ts = text.length();
        for (int j = 0; j < ts; j++){
            char letter = text[j];
            if(isalpha(letter)){
                if (!letters.count(toupper(letter))){
                    letters.insert(toupper(letter));
                }
            }
        }
        int ls = letters.size();
        if (ls == 26){
            cout << "frase completa" << endl;
        } else if(ls >= 13){
            cout << "frase quase completa" << endl;
        } else {
            cout << "frase mal elaborada" << endl;
        }
    }
    return 0;
}