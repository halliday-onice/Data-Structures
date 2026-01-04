#include <limits.h>
#include <stdio.h>
#include <stdlib.h>

struct stack{
  int top;
  unsigned capacity;
  int *array;
};


struct stack* createStack(unsigned capacity){
    struct stack *newStack = (struct stack*) malloc(sizeof(struct stack));
    newStack->capacity = capacity;
    newStack->top = -1;

    newStack->array = (int*) malloc(newStack->capacity * sizeof(int));
    return newStack;
}

int isFull(struct stack *stack){

    return stack->top == stack-> capacity - 1; // the -1 is bc we are implementing using vector and its length varies
    // from 0 to capacity - 1
}

int isEmpty(struct stack *stack){

    return stack->top == -1;


}



void push(struct stack *stack, int item){

    printf("entered push function\n");
    if(isFull(stack))
        return;

    printf("after check if it is empty\n");

    // incrementa primeiro e DEPOIS (apos o incremento) assimilamos ao novo valor
    // no array.
    stack->array[++stack->top] = item; // adiciona o item novo ao
    printf("PUSHED %d  successfuly\n", item);
    //printf("Stack capacity %d\n", stack->capacity);

}

int pop(struct stack *stack)
{
    if(isEmpty(stack)){
        return INT_MIN;
    }
    return stack->array[stack->top--];
}

void printStack(struct stack *stack)
{
    if(isEmpty(stack)){
        printf("Stack is empty\n");
    }
    printf("STACK\n");
    for(int i = stack->top; i >= 0 ;i--){
        printf("\n %d ",stack->array[i]);
    }
    printf("\n");

}

int main(){

    struct stack* stack = createStack(100);

    push(stack, 15);
    push(stack, 22);
    push(stack, 108);



    printStack(stack);


    pop(stack);

    printStack(stack);

    pop(stack);

    printStack(stack);




    return 0;
}
