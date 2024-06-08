#include <stdio.h>
#include <stdlib.h>


int countDigits(int n){
    int counter = 0;
    while(n > 0){
        counter += 1;
        n = n / 10;
        printf("counter: %d\n", counter);
        printf("n: %d\n", n);
    }
    return counter;
}


int main(){
    int input;
    scanf("%d", &input);

    int res = countDigits(input);

    printf("%d\n", res);



    return 0;
}
