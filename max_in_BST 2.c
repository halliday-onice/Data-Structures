#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node *left, *right;
};

struct node *newNode(int newData){
    struct node *new =(struct node*) malloc(sizeof(struct node));
    new->data = newData;
    new->left = new->right = NULL;
    return new;

}

int max(int a, int b)
{
    if(a >= b)
        return a;
    else
        return b;
}

int maxx_value = 0;
void find_max_in_BST(struct node *root)
{
    if(root == NULL)
        return;
    maxx_value = max(maxx_value, root->data);
    find_max_in_BST(root->left);
    find_max_in_BST(root->right);


}


int main(){
    return 0;
}
