#include<stdio.h>
#include <stdlib.h>


/* IN PRE ORDER TRAVERSAL THE ORDER IS ROOT-LEFT-RIGHT */
struct nodeTree{
    int data;
    struct nodeTree *left;
    struct nodeTree *right;
};

struct nodeTree *newNode(int newData){
    struct nodeTree *node = (struct nodeTree*) malloc(sizeof(struct nodeTree));
    node->data = newData;
    node->left = node->right = NULL;

    return node;
}

void printPreOrder(struct nodeTree* node){
    if(node == NULL)
        return;
    printf("%d ", node->data);

    printPreOrder(node->left);

    printPreOrder(node->right);



}





int main(){
    struct nodeTree* root = newNode(1);
	root->left = newNode(2);
	root->right = newNode(3);
	root->left->left = newNode(4);
	root->left->right = newNode(5);


    printf("Pre order traversal of binary tree is \n");
    printPreOrder(root);



    return 0;
}
