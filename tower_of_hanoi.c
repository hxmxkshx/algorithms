#include<stdio.h>

void func(int n, int from, int to){
  int temp;
  if(n == 1)
    printf("%d => %d\n", from, to);
  else{
    temp = 6 - from - to;
    func(n-1, from, temp);
    printf("%d => %d\n", from, to);
    func(n-1, from, temp);
  }
}

int main(){
  func(4, 1, 3);
  return 0;
}