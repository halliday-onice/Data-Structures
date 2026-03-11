#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct node {
    int data;
    struct node *next;
};


void printList(struct node *head)
{
    struct node *aux = head;


    while(aux != NULL){
        printf("%d ->", aux->data);
        aux = aux->next;
    }
    printf("\n");




}

struct node *searchItem(struct node *root, int item)
{
    struct node *aux = root;

    while(aux != NULL)
    {
        if(aux->data == item){
            return aux;
        }

        aux = aux->next;
    }
    return NULL;


}

void insertAtPosition(struct node *root, int pos, int dataToInsert)
{
    struct node *new_node = (struct node*)malloc(sizeof(struct node));
    new_node->data = dataToInsert;

    struct node *aux = root;
    if(pos == 1){
        new_node->next = root;
        root = new_node;
        return;
    }
    for(int i =0;i < pos - 1; i++){
        aux = aux->next;
    }
    new_node->next = aux->next;
    aux->next = new_node;

}

void insertAtLast(struct node *root,int datatoInsert)
{
    struct node *aux = root;
    struct node *new_node = (struct node*) malloc(sizeof(struct node));
    new_node->data = datatoInsert;
    new_node->next = NULL;

    if(root == NULL){
        root = new_node;
        return;
    }

    while(aux != NULL && aux->next!=NULL){
        aux = aux->next;
    }
    aux->next = new_node;
}

struct node *search(struct node *head,int item){
    struct node *headnext = head->next;
    struct node *aux = head;

    if(aux == NULL)
        return false;
    if(aux->data == item)
        return aux;
    aux = aux->next;

    return search(head->next,item);

}
void deleteFirst(struct node *root){

    if(root == NULL)
        return;
    struct node *temp = root;
    struct node *aux = root->next;
    temp = aux;

    free(temp);




}

int main(){
    struct node *cab = (struct node*) malloc(sizeof(struct node));
    cab->data = 1;
    cab->next = NULL;
    insertAtLast(cab,10);
    insertAtLast(cab,5);
    insertAtLast(cab,15);
    insertAtPosition(cab, 4,12); // insercao em uma posicao especifica
    insertAtLast(cab,20);

    printList(cab);

    deleteFirst(cab); // ta dando ruim por conta do null no inicio
    //printList(cab);


    return 0;
}
