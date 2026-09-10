
#include <stdio.h>
#include <stdlib.h>

/* You are given a number n. You need to find the digital root of n.
DigitalRoot of a number is the recursive sum of its digits until we get a single digit number.


 */

int digitalRoot(int n){
    int counter = 0;
    int sum = 0;
    int remainder = 0;

    while(n > 0 ){

        counter += 1; // incrementa o contador dos digitos
        remainder = n % 10; // vai somando na variavel
        sum += remainder;
        n = n / 10; // vai andando entre as casas decimais
        printf("counter: %d\n", counter);
        printf("sum: %d\n", sum);
        printf("remainder: %d\n", remainder);
        puts("++++++");
    }
    if(sum > 9){ //se a funcao for maior que o um numero com mais de um algarismo, chama a funcao de novo
        return digitalRoot(sum);
    }
    return sum;


}




int main(){

    int input = 99999;
    //scanf("%d", &input);

    int res = digitalRoot(input);

    printf("%d\n", res);

    return 0;
}
