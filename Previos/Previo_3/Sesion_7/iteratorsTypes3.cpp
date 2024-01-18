#include <iostream>
#include <vector>
using namespace std;

int main() {
  // creando ub vector
  vector<int> vec{1, 2, 3, 4};

  // creando iteradores que apuenten a los primeros y ultimos elementos
  vector<int>::iterator itr_first = vec.begin();
  vector<int>::iterator itr_last = vec.end() - 1;

  //muestra el vector elementos
  cout << "First Element: " << *itr_first << endl;
  cout << "Second Element: " << itr_first[1] << endl;

    cout << "Second Last Element: " << *(itr_last - 1) << endl;
    cout << "Last Element: " << *itr_last << endl;

  return 0;
}
