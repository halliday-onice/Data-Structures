#include <stdio.h>
#include <stdlib.h>

// This implementation of a list using a linked list 
// in a list we insert in the END and delete in the beginning
//  
//
//



struct nodeFila{
	int value;
	struct node *next;
}


//  
// 
//
struct fila{
	struct node *ini;
	struct node *end;
};

struct fila *create(){
	struct f = (struct fila*) malloc(sizeof(struct fila));
	f->ini = f->end = NULL;
	return f;
}


void insert(struct fila *f,int newValue){
	struct nodeFila *node = (struct nodeFila*) malloc(sizeof(struct nodeFila));
	node->value = newValue;
	node->next = NULL;

	if(f->end != NULL) // see if the list is NOT empty
		f->end->next = node;
	else // see if the list is empty
		f->ini = node;
	f->end = node;

}



void printList(struct fila *f){
	for(struct node* no = f->ini; no != NULL; no = no->next)
		printf("%d -> ",no->value);
	printf("\n");
}

int main(){



	return 0;
}