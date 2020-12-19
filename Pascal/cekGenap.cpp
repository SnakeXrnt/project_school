#include <cstdio>

bool cekGenap(int number){
  if (number % 2 == 0){
    return true;
  } else {
    return false;
  }
}

int main(){
  int myNumber = 10;
  if (cekGenap(myNumber))
  {
    printf('Genap\n')
  } else {
    printf('ganjil\n')
  }
}
