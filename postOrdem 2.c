#include <stdio.h>
#include <stdlib.h>

//the order of the traversing is LEFT-RIGHT-ROOT


struct nodeTree {
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

void printPostOrdem(struct nodeTree *node){
    if(node ==  NULL)
        return;
    printPostOrdem(node->left);
    printPostOrdem(node->right);
    printf("%d ", node->data);
}

int main(){
    struct nodeTree* root = newNode(1);
	root->left = newNode(2);
	root->right = newNode(3);
	root->left->left = newNode(4);
	root->left->right = newNode(5);


    printf("Post order traversal of binary tree is \n");
    printPostOrdem(root);


    return 0;
}
