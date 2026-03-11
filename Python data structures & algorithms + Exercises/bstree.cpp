#include <iostream>
#include <memory>

using namespace std;

/*  Binary search tree
*	the left subtree of a node contains only nodes with keys lesser than the node's key
*	the right subtree of a node contains only nodes with keys greater than the node's key
*	repetition is not allowed
*/
// auto something = std::make_unique<std>
/* smart pointers
	unique_ptr<A> ptr (new A)
	*/
class BinaryTree
{
	struct node{
		int key;
		struct node *left;
		struct node *right;
	};


	// trying to do it recursively
	struct node* search(struct node* root, int key)
	{
		if(root == NULL || root->key == key) 
			return NULL;

		if(key > root->key) //se chave for maior, keep search -desce subarvore dir
			return search(root->right,key);

		return search(root->left, key); // se nao, keep search -desce subarvore esq

	}

}


int main()
{

}