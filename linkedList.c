#include <stdio.h>
#include <stdlib.h>


struct nodeList {
      int data;
      struct nodeList *next;
};

struct nodeList *head = NULL;

void printList()
{
      struct nodeList *aux = head;
      while(aux != NULL)
      {
            printf(" %d ->", aux->data);
            aux = aux->next;
      }
}

void insertItem(int newItem)
{
      struct nodeList *newNode = (struct nodeList*) malloc(sizeof(struct nodeList));

      newNode->data = newItem;
      newNode->next = head; // inserindo no inicio
      head = newNode;
}

void traverseList(struct nodeList *head){
      if(head == NULL)
            return;
      
      printf("%d", head->data);

      traverseList(head->next);
}
/*
void insertItemEnd(int data){
      struct nodeList
}
*/

int main(){

    insertItem(10);
    insertItem(5);
    insertItem(15);
    insertItem(20);
    
    printList();



      return 0;
}