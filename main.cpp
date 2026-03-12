#include <iostream>
using namespace std;

void swapValues(int* p1, int* p2) {
    int temp = *p1;
    *p1 = *p2;
    *p2 = temp;
}


void printArray(int* arr, int size) {
    for(int i = 0; i < size; i++) {
        cout << *(arr + i) << " ";
    }
    cout << endl;
}


int findSum(int* arr, int size) {
    int sum = 0;
    for(int i = 0; i < size; i++) {
        sum += *(arr + i);
    }
    return sum;
}


void shiftRight(int* arr, int size) {
    int last = *(arr + size - 1);

    for(int i = size - 1; i > 0; i--) {
        *(arr + i) = *(arr + i - 1);
    }

    *arr = last;
}

int* createArray(int size) {
    int* arr = new int[size];
    return arr;
}

void deleteArray(int* arr) {
    delete[] arr;
}


int main() {
    int n;
    int sum=0;
    int size=0;


    cout << "Enter array size: ";
    cin >> n;
    size = n;

    int arr[n];

    cout << "Enter values: ";

    for(int i = 0; i < n; i++) {
        cin >> arr[i];
        cout<< i+1 << ". sayi " << arr[i]<<endl;
        sum+=arr[i];

    }
    cout<<"total sum of numbers "<<sum<<endl;
    cout<<"-------------------------------";
    cout<<"\n a,b ikilisi girin";
    int a , b ;
    cin>>a>>b;

    cout << "\nBefore swap\n";
    cout << "a = " << a << endl;
    cout << "b = " << b << endl;

    swapValues(&a, &b);

    cout << "\nAfter swap\n";
    cout << "a = " << a << endl;
    cout << "b = " << b << endl;

    cout << "\n----------------------------------\n";
    cout << "Shifting array right...\n";

    shiftRight(arr, size);

    cout << "\n after shiftRight:\n";
    printArray(arr, size);

    cout << "\n-----------------------------------\n";

    cout << "Deleting array\n";
    deleteArray(arr);

    return 0;
}