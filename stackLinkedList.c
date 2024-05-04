#include <stdio.h>
#include <stdlib.h>

struct nodeStack{
    int data;
    struct nodeStack *next;

};

struct nodeStack *head = NULL;

void pushNode(struct nodeStack *node, int newValue)
{
    struct nodeStack *newNode = (struct nodeStack*) malloc(sizeof(struct nodeStack));
    newNode->data = newValue;
    newNode->next = head;
    head = newNode; // como eh a pilha a head tem que ficar sempre por cima

}

void pop()
{
    //create a temporary node
    struct nodeStack *temp;

    if(head == NULL)
        printf("Stack is empty\n");

    printf("poped element: %d\n", head->data);

    temp = head;

    head = head->next;

    free(temp);
}

void printStack(struct nodeStack *stack)
{
    struct nodeStack *aux = head;
    printf("STACK\n");
    while(aux != NULL){
        printf("%d ->",aux->data);
        aux = aux -> next;
    }
    printf("\n");

}



int main(){

    struct nodeStack *stack;
    pushNode(stack, 20);
    printStack(stack);
    pushNode(stack,33);
    pushNode(stack, 55);
    printStack(stack);
    pop();
    printStack(stack);


    return 0;
}
