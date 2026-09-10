#include <stdio.h>
#include <stdlib.h>

int sumOfDigits(int n){
    int counter = 0;
    int sum = 0;
    while(n > 0){
        sum += n % 10;
        n = n / 10;
        //printf("counter: %d\n", counter);
        //printf("n: %d\n", n);
        //printf("sum: %d\n", sum);

    }
    return sum;
}





int main(){

    int input = 99999;
    int res = sumOfDigits(input);

    printf("%d\n",res);


    return 0;
}
