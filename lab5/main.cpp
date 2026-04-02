#include <iostream>
using namespace std;

// Question 1: factorial (recursive)
int factorial(int x) {
    if (x == 0 || x == 1)
        return 1;
    else
        return x * factorial(x - 1);
}


// Question 2: e^x calculation
double exp_x(int x, int n) {
    double total = 0;

    for (int i = 0; i <= n; i++) {
        // term = (x^i) / i!

        // x^i hesapla
        double power = 1;
        for (int j = 0; j < i; j++) {
            power = power * x;
        }

        double term = power / factorial(i);
        total = total + term;
    }

    return total;
}


// Question 3 & 4: alternating series (recursive, return var)
double series(int n) {
    if (n == 1)
        return 1;

    if (n % 2 == 0)
        return series(n - 1) - (1.0 / n);
    else
        return series(n - 1) + (1.0 / n);
}


// MAIN
int main() {

    // 1
    int num;
    cout << "Enter number for factorial: ";
    cin >> num;
    cout << "Factorial = " << factorial(num) << endl;

    cout << endl;

    // 2
    int x, n;
    cout << "Enter x: ";
    cin >> x;
    cout << "Enter n: ";
    cin >> n;

    cout << "e^x approximation = " << exp_x(x, n) << endl;

    cout << endl;

    // 3 & 4
    int n2;
    cout << "Enter n for series: ";
    cin >> n2;

    cout << "Series result = " << series(n2) << endl;

    return 0;
}