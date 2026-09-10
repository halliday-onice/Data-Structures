#include <stdio.h>
#include <stdlib.h>
/* Insert in the end of the linked list */


struct node {
    int data;
    struct node *next;
}*head;


void insertEnd(int newData)
{
    struct node *newNode, *temp;

    newNode  = (struct node*) malloc(sizeof(struct node));

    newNode->data = newData;
    newNode->next = NULL; // como estamos inserindo no fim, o proximo do ultimo node eh o fim, ou seja o ultimo, portanto newNode-> next = NULL
    temp = head;

    if(head == NULL){
        head = newNode;
        return;
    }


    while(temp != NULL && temp->next != NULL)
    {
        temp = temp->next;

    }
    temp->next = newNode; // apos o while o temp vai estar no ultimo node, aqui apenas atualizo o seu valor



}

void printList()
{
      struct node *aux = head;
      while(aux != NULL)
      {
            printf(" %d ->", aux->data);
            aux = aux->next;
      }
      printf("\n");
}


int main()
{
    insertEnd(10);
    insertEnd(22);
    printList();
    insertEnd(555);
    printList();

    return 0;
}
