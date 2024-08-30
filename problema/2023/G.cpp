#include <iostream>
#include <cmath>

using namespace std;

int main() {
    double v, p, total;
    cin >> v >> p;
    total = v * p;
    for (double i = 10; i < 100; i += 10) {
        double prod = total * i;
        long long calc = ceil(prod / 100);
        cout << calc;
        if (i != 90) cout << " ";
    }
    cout << endl;
    return 0;
}
