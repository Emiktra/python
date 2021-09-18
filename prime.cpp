#include <iostream>

bool isPrime(int num) {
  if (num > 1){
   for (int i=2; i<num; i++){
     if(num%i==0){
       return false;
     }
   } 
  } 
  else{
    return false;
  }
  return true;
}

int main(){
    std::cout << isPrime(7) << std::endl;
    return 0;
}