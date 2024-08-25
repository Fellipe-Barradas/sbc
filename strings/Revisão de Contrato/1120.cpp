#include <iostream>
#include <string>
#include <cctype>

using namespace std;

int main(){
    int digit;
    string text;
    while (cin >> digit >> text && text[0] != '0'){
        string res = "";
        for (size_t i = 0; i < text.size(); i++) {
            int ltn = text[i] - '0';
            if (ltn != digit){
                if (res.length() == 0 && ltn != 0){
                    res.push_back(text[i]);
                }else if (res.length() > 0){
                    res.push_back(text[i]);
                }
                
            }
        }
        if (res != ""){
            cout << res << endl;
        }else{
            cout << "0" << endl;
        }
       
    }

    return 0;
}