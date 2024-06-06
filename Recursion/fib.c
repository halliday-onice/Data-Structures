#include <stdio.h>
#include <stdlib.h>



int fib(int n){
    if(n <= 1) // if (n == 0) return 0 if (n == 1) return 1. fib(0) = 0 e fib(1) = 1
        return 1;


    return fib(n - 1) + fib(n - 2);
    //n = 5
    // fib(4) + fib(3)
    // n = 4
    // fib(3) + fib(2)
    // n = 3
    // fib(2) + fib(1) = 1
    // n = 2
    // fib(1) = 1 + fib(0)= 1
}


int main(){
    int res = fib(4);
    printf("%d\n", res);




    return 0;
}
