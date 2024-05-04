#include <stdio.h>
#include <stdlib.h>


typedef struct lista LISTA;
typedef struct node LISTANO;

struct lista{
	LISTANO* prim;
};

struct node {
	int inf;
	LISTANO* prox;
};


 LISTA* cria(void){
	LISTA* l = (LISTA*) malloc(sizeof(LISTA));
	l->prim = NULL;
	return l;
}
//funcao de inserção
void insere(LISTA* l,int valor){
	LISTANO* novo = (LISTANO*) malloc(sizeof(LISTANO));
	novo->inf = valor;
	novo->prox = l->prim;
	l->prim = novo;

	printf("Elemento %d inserido no início da lista com sucesso\n",valor);

}

void lst_imprime(LISTA* l){
	for(LISTANO* p= l->prim; p!= NULL;p = p->prox)
		printf("%d ",p->inf);
	printf("\n");
}

//funcao que verifica se um elemento está na lista
int pertence(LISTA* l,int value){
	for(LISTANO* p=l->prim; p!= NULL;p = p->prox){
		if(p->inf== value)
			//printf("Elemento está na lista\n");
			return 1;
	}
	//printf("Elemento não está na lista\n");
	return 0; // nao encontrou
}

//funcao insere em ordem

void insere_ordem(LISTA* l, int valor){
	LISTANO* ant = NULL; // ponteiro para elemento anterior
	LISTANO* p = l->prim; // ponteiro para percorrer a lista

	//localiza a posicao de insercao
	while(p != NULL && p->inf < valor){
		ant = p;
		p = p->prox;
	}

	//lista com novo elemento
	LISTANO* novo = (LISTANO*) malloc(sizeof(LISTANO));
	novo->inf = valor;

	//encadeia o elemento
	if(ant == NULL){ //insere elementos no inicio
		novo->prox = l->prim;
		l->prim = novo;

	}
	else{ //insere elemento no meio da lista
		novo->prox = ant->prox;
		ant->prox = novo;
	}
}

//funcao que retira elemento da lista
void retirar(LISTA* l, int valor){
	LISTANO* ant = NULL; //ponteiro p elemento anterior
	LISTANO* p = l->prim; //ponteiro para percorrer a lista


	//procura elemento na lista guardando anterior
	while(p != NULL && p->inf != valor){
		ant = p;
		p = p->prox;
	}

	if(p != NULL){ //verifica se achou elemento
		//retira elemento
		if(ant == NULL){
			l->prim = p->prox; //retira elemento do inicio

		}
		else{
			ant->prox = p->prox;

		}
		free(p);

	}
}
//funcao de liberar a fila
void lista_libera(LISTA* l){
	LISTANO* p = l->prim;
	while(p != NULL){
		LISTANO* t = p->prox; //guarda a referencia p/ prox elemento 
		free(p); //libera a memoria apontada por p
		p = t; //faz p apontar para o proximo
	}
	free(l);

}


int main(){


	LISTA* l = cria();
	insere(l,23);
	insere(l,34);
	insere(l,22);
	insere(l,33);
	//LISTANO* prox = cria();

	insere_ordem(l,21);

	lst_imprime(l);

	if(pertence(l,33) == 0){
		printf("Está na lista\n");
	} else {
		printf("Não está na lista\n");
	}
	retirar(l,23);
	lst_imprime(l);




	return 0;
}