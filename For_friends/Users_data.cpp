/* 
Задача.
Додавати користувачів до списку в залежності від їх віку.
За default користувачів записують у файл users
Але, якщо користувачу менше 18, то він буде додатково записаний у файл ch_users
*/
#include <iostream>
#include <cstring>
#include <fstream>

using namespace std;

int main(){

    //block_1
    char name[20] = "";
    cout<<"Enter your nickname : " ;
    cin>>name;
    
    //block_2
    int age = 0;
    cout<<"Enter your age : ";
    cin>>age;
    
    //if block
    char path[20] = "users.txt";
    if(age >= 18){  }

    else{
        char path[20] = "ch_users.txt";
        ofstream outfile;
        outfile.open(path, std::ios::app);
        outfile << name << ' ' << age << endl;
        outfile.close();
    }
    
    //block_3
    ofstream outfile;
    outfile.open(path, std::ios::app);

    //block_4
    outfile << name << ' ' << age << endl;
    outfile.close();

    //block_5
    cout<<"User added successfully !";
    
return 0;
}
