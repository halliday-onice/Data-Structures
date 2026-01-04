#include <stdio.h>
#include <stdlib.h>


void print1ToN(int curr, int end) {
    if (curr > end){
        return;
    }
    printf("%d\n", curr);
    print1ToN(curr + 1, end);
}



int main() {
    print1ToN(5, 145);


    return 0;
}
