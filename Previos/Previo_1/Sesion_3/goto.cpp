#include <iostream>
using namespace std;

int main()
{
    float num, average, sum = 0.0;
    int i, n;

    cout << "Numero Maximo de inputs: ";
    cin >> n;

    for (i = 1; i <= n; ++i)
    {
        cout << "Ingrese n" << i << ": ";
        cin >> num;

        if (num < 0.0)
        {
            // Control de el programa para saltar a jump:
            goto jump;
        }

        sum += num;
    }

jump:
    average = sum / (i - 1);
    cout << "\nAverage = " << average;

    return 0;
}
