#include <iostream>
#include <string>
#include <vector>

using namespace std;

struct Letter{
    char value;
    int pos;
};

bool eVogal(char ch){
    return 'a' == ch || 'e' == ch || 'i' == ch || 'o' == ch || 'u' == ch;
}

vector<Letter> separateLetter(string &text, bool vogals){
    vector<Letter> list;
    int ts = text.size();
    for (int i = 0; i < ts; ++i) {
        char ch = text[i];
        bool isVowel = eVogal(ch);

        if (vogals && isVowel) {
            list.push_back(Letter{ch, i});
        } else if (!vogals && !isVowel) {
            list.push_back(Letter{ch, i});
        }
    }
    return list;
}

void tranform_string(string &text, int deslocamento, bool vogais){
    vector<Letter> lletter = separateLetter(text, vogais);
    int i = 0;

    for(Letter letter : lletter){
        int segunda_pos = i;
        int target_pos = (segunda_pos + deslocamento) % lletter.size();
        text[letter.pos] = lletter[target_pos].value;
        i++;
    }
}


int main(){
    int numTests, counter;
    cin >> numTests;
    counter = 1;
    while (numTests--) {
        string text;
        cin >> text;

        int numInstructions;
        cin >> numInstructions;

        cout << "Caso #" << counter << ":" << endl;
        while (numInstructions--) {
            int tipo, passos;
            cin >> tipo;
            switch (tipo){
            case 0:
                cin >> passos;
                tranform_string(text, passos, true);
                break;
            case 1:
                cin >> passos;
                tranform_string(text, passos, false);
                break;
            default:
                cout << text << endl;
                break;
            }
        }

        counter+=1;
    }
    return 0;
}