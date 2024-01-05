#include <iostream>
using namespace std;



void test(){
    // Var es una var estatica
    static int var = 0;
    ++var;
    
    cout << var << endl;

}


int main(){

    test();
    test();
    


    return 0;
}