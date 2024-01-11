#include <iostream>
using namespace std;

int main() {
    int num;
    cout << "Enter total number of students: ";
    cin >> num;
    
    // memory allocation of num number of floats
    float* ptr;
    ptr = new float[num];

    cout << "Enter GPA of students: " << endl;
    for (int i = 0; i < num; ++i) {
        cout << "Student " << i + 1 << ": ";
        cin >> *(ptr + i);
    }

    cout << "\nDisplaying GPA of students." << endl;
    for (int i = 0; i < num; ++i) {
        cout << "Student " << i + 1 << " : " << *(ptr + i) << endl;
    }

    // ptr memory es liberado o released
    delete[] ptr;

    return 0;
}
