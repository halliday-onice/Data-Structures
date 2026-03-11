#include <stdio.h>
#include <stdlib.h>

struct treeNode{
      int data;
      struct treeNode *left;
      struct treeNode *right;

};

struct treeNode *newNode(int newData){
      struct treeNode *treeNode =  (struct treeNode*) malloc(sizeof(struct treeNode));
      treeNode->data = newData;
      treeNode->left = NULL;
      treeNode->right = NULL;

      return treeNode;

}
void printInOrder(struct treeNode* node){
      if(node == NULL){
            return;
      }
      printInOrder(node->left);
      // faz o print do dado
      printf("%d ", node->data);

      printInOrder(node->right);
}



int main(){
      struct treeNode* root = newNode(1);
	root->left = newNode(2);
	root->right = newNode(3);
	root->left->left = newNode(4);
	root->left->right = newNode(5);

      printf("Inorder traversal of binary tree is \n");
	printInOrder(root);
    

      return 0;
}