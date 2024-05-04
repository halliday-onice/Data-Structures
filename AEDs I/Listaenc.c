#include <stdio.h>
#include <stdlib.h>


struct list{
	int v;
	struct list *next;
	//struct list *head; // this node represents the beggining of the linked list


};

// void alocateNodeList(struct list *l){
// 	struct list *l = (struct list*) malloc(sizeof(struct list));
// 	l->head = l;
// 	l->
	
	
// }

// this function is to insert 
// an integer right in the beggining  
//
//
void insertHead(struct list **head_ref,int newvalue)
{
	struct list* newNode = (struct list*) malloc(sizeof(struct list));

	newNode->v = newvalue;
	printf("newvalue int: %d\n",newvalue);
	newNode->next = (*head_ref);
	(*head_ref) = newNode;
	
}


void printLinkedlist(struct list *l){
	printf("List - ");
	struct list *temp = l;

	printf("l->v: %d\n",l->v);
	while(temp!= NULL){
		printf("-> %d ", temp->v);
		temp = temp->next;
	}
	printf("\n");
}


int main()
{
	struct list *l = (struct list*) malloc(sizeof(struct list));
	insertHead(&l,2);
	insertHead(&l,3);
	insertHead(&l,5);
	printLinkedlist(l);
	return 0;
}