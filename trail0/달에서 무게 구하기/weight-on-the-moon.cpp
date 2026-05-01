#include <iostream>
using namespace std;

int main() {
    const float moon_g = 0.165;
    int choo = 13;

    cout << fixed;
    cout.precision(6);

    cout << choo << " * " << moon_g << " = " << choo*moon_g;
    return 0;
}