#include <iostream>
#include <cstring>
using namespace std;
int main(){
   char a[]="Vladyslav";
   char b[10] = "";
   strncpy(b,a,4);
   cout<<b;
return 0;
}