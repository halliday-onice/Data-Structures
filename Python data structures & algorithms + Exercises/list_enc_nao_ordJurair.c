#include "stdlib.h"
#include "stdio.h"

struct no {
	int c;
	struct no *prox;
};

/* Efetua a busca do elemento k, e retorna o
   ponteiro do nó anterior (caso encontre).
   Caso contrário, retorna NULL.
*/
struct no * buscar(struct no *cab, int k) {
	struct no *pont = cab;
	struct no *p = cab->prox;
	while (p != NULL) {
		if (p->c == k) {
			return pont;
		}

		pont = p;
		p = p->prox;
	}

	// Se chegar até aqui, significa que não achou o elemento.
	return NULL;
}

/* Lista não ordenada, então inserção irá ocorrer
   no início (após o nó cabeça auxiliar)
*/
void inserir(struct no *cab, int k) {
	struct no *pont = buscar(cab, k);
	if (pont == NULL) {
		struct no *p = (struct no*)malloc(sizeof(struct no));
		p->c = k;

		// Atualização dos ponteiros.
		p->prox = cab->prox;
		cab->prox = p;

		printf("Elemento %d inserido no início da lista com sucesso.\n", k);
	} else {
		printf("Elemento %d já contido na lista.\n", k);
	}
}

/* Efetuar a busca.
   Caso encontre o elemento, efetua a remoção.
*/
void remover(struct no *cab, int k) {
	struct no *pont = buscar(cab, k);
	if (pont != NULL) {
		struct no *p = pont->prox;
		pont->prox = p->prox;
		free(p);

		printf("Elemento %d removido com sucesso.\n", k);
	} else {
		printf("Elemento %d não está contido na lista.\n", k);
	}
}

void imprimir(struct no *cab) {
	printf("Lista - ");

	struct no *p = cab->prox;
	while (p != NULL) {
		printf("%d ", p->c);
		p = p->prox;
	}
	printf("\n");
}

int main() {
	struct no *cab = (struct no*)malloc(sizeof(struct no));

	inserir(cab, 1);
	inserir(cab, 2);
	//inserir(cab, 2);
	inserir(cab, 3);
	//inserir(cab, 3);

	// Lista - 3 2 1
	imprimir(cab);

	printf("\n");

	remover(cab, 10);
	//remover(cab, 1);
	//remover(cab, 2);
	//remover(cab, 3);

	imprimir(cab);

	return EXIT_SUCCESS;
}