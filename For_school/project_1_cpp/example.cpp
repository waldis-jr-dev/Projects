#include <iostream>
#include <curses.h>
#include <cstring>
using namespace std;
int main() {
    char s[20], f[20], sr[20], a[20];
    int l, ll;
    cout<<"\n Input stroky s:\n" ;
    cin>>s;
    cout<<"Input stroky f:\n";
    cin>>f;
    l = strlen(s);
    cout<<"\n Dlina stroki s=" << l;
    ll = strlen(f);
    cout<<"\n Dlina stroki f=" << ll;
    strcat(s,f);
    strcpy(sr,s);
    cout<<"\n Novaya stroka" << sr;
    strncpy(sr,"eeeeee",4);
    cout<<"\n Novaya stroka=" << sr;
return 0;
}