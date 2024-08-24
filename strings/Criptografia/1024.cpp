    #include <iostream>
    #include <cctype>
    #include <cmath>
    #include <stack>
    #include <string>
    using namespace std;

    int main(){
        int N;
        cin >> N;
        cin.ignore();

        for(int i = 0; i < N; i++){
            string text;
            stack<char> p;
            cin.clear();
            getline(cin, text);
            cout << "texto: " << text << endl;
            int ts = text.size();
            for (int j = 0; j < ts; j++){
                if (isalpha(text[j])){
                    p.push((char)(text[j] + 3));
                }else if(!isspace(text[j])){
                    p.push(text[j]);
                }else if(isspace(text[j]) && j > 0){
                    p.push(text[j]);
                }
            }
            string res;
            while(!p.empty()){
                if((int)p.size() <= ceil(ts / 2)){
                    res += p.top() - 1;
                    p.pop();
                }else{
                    res += p.top();
                    p.pop();
                }

            }
            cout << res<< endl;
        }
        return 0;
    }