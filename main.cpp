#include <iostream>
using namespace std;

int main() {
    int num;
    int steps = 0;

    cout << "1 den buyuk bir sayi girin: ";
    cin >> num;

    cout << num;

    while (num != 1) {
        if (num % 2 == 0) {
            num = num / 2;
        } else {
            num = num * 3 + 1;
        }

        cout << " -> " << num;
        steps++;
    }

    cout << "\nToplam adim: " << steps << endl;

    /////////////////////////////////////////////////////////////task2
    int n;

    cout << "Enter a number between 10 and 100: ";
    cin >> n;

    while (n < 10 || n > 100) {
        cout << "Invalid! Enter a number between 10 and 100: ";
        cin >> n;
    }

    int fizz_count = 0;
    int buzz_count = 0;
    int fizzbuzz_count = 0;

    for (int i = 1; i <= n; i++) {

        if (i % 7 == 0) {
            cout << i << " skipped" << endl;
            continue;
        }

        if (i % 3 == 0 && i % 5 == 0) {
            cout << "FizzBuzz" << endl;
            fizzbuzz_count++;
        }
        else if (i % 3 == 0) {
            cout << "Fizz" << endl;
            fizz_count++;
        }
        else if (i % 5 == 0) {
            cout << "Buzz" << endl;
            buzz_count++;
        }
        else {
            cout << i << endl;
        }
    }

    cout << "Summary:" << endl;
    cout << "Fizz: " << fizz_count << endl;
    cout << "Buzz: " << buzz_count << endl;
    cout << "FizzBuzz: " << fizzbuzz_count << endl;
/////////////////////////////////////////////////////////////////task3
    int nem;

    cout << "Enter a number between 3 and 9: ";
    cin >> nem;

    while (nem < 3 || nem > 9) {
        cout << "Invalid! Enter a number between 3 and 9: ";
        cin >> nem;
    }

    // üst kısım
    for (int i = 1; i <= nem; i++) {
        for (int j = 0; j < i; j++) {
            cout << "*";
        }
        cout << endl;
    }

    // alt kısım
    for (int i = nem - 1; i > 0; i--) {
        for (int j = 0; j < i; j++) {
            cout << "*";
        }
        cout << endl;
    }

    return 0;
}