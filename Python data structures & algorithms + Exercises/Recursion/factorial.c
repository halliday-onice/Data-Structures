#include<stdio.h>
#include <stdlib.h>


int factorial(int n){

    if(n == 0)
        return 1;




    return n * factorial(n - 1);

}

int main() {
    int result;
    result = factorial(5);
    printf("%d\n",result);


    return 0;
}
