
// Aluno: Jonatas Halliday Sant Anna do Nascimento
#include <stdio.h>
#include <stdlib.h>

//typedef struct lista LISTA;
typedef struct listano NOLISTA;

/*struct lista{
	NOLISTA *cab;
	NOLISTA* ult;
	

}; */

struct listano {
	int value;
	NOLISTA *ant;
	NOLISTA *prox;

}; 

void criar(NOLISTA* cab){
	
	cab->prox = cab;
	cab->ant = cab;


	/*cab->prox = ult;
	cab->ant = ult;
	ult->ant = cab;
	ult->prox = cab;
	*/
	
} 

//funcao busca
NOLISTA* busca(NOLISTA* cab,int v){
	
	NOLISTA* p = cab->prox;
	//printf("chega\n");
	while(p!= cab){

		//printf("%p\n",cab);
		//printf("%p\n",p);
		
		if(p->value == v){

			return p;
		}
		p = p->prox; //aqui eu atualizo o valor de p, ou seja eu ando na lista

		
	}

	//printf("chega2\n");

	return cab;


	
}

//busca dupla
NOLISTA* busca2(NOLISTA* cab,NOLISTA* ult,int v)
{
	NOLISTA* pont = cab;
	NOLISTA* p = cab->prox;
	ult->value = v + 1;

	if((p->ant == cab) && p == ult)
		return cab;
	return NULL;
}


void imprimir(NOLISTA* cab){
	//p eh o ponteiro auxiliar para andar na Lista
	printf("LISTA - ");
	NOLISTA *p = cab->prox;
	while(p != cab){
		printf("%d ",p->value);
		p = p->prox;
	}
	printf("\n");


}

/*	//p eh o ponteiro auxiliar para andar na Lista
*/


void insere1(NOLISTA* cab,int v){

	NOLISTA* pont = busca(cab,v);
	//printf("ui\n");
	
	
	//printf("cabeca:%p\n",cab);
	//printf("pont:%p\n",pont);
	if(pont==cab){
		NOLISTA* novo = (NOLISTA*) malloc(sizeof(NOLISTA));
		NOLISTA* x = cab->prox;
		//printf("alo1");
		
		novo->value= v; // conteudo dentro da "caixa" novo eh o v
		novo->ant = cab; //pra quem novo aponta
		novo->prox = x; //eh a seta vermelha do desenho novo->x
		//atualizacao dos ponteiros
		cab->prox = novo; //agora cab->prox eh o novo, antes apontava pra x
		x->ant = novo; //antes apontava pro cabeça e agr aponta pro nov

		//printf(" cabeca->prox: %p cabeca->ant: %p novo->prox: %p novo->antes:%p\n",cab->prox,cab->ant,novo->prox,novo->ant);

		
	} else{
		printf("\n");
		printf("Elemento já contido na lista\n");
		printf("\n");
		//printf("Elemento já contido\n");

	}
	

}

void insere_ord(NOLISTA *cab, int v){
	NOLISTA* pont = busca(cab,v);
	NOLISTA* p = cab->prox;
	//NOLISTA* ant = cab;
}

void retira(NOLISTA *cab,int v){
	NOLISTA* p = busca(cab,v);

	if(p== NULL){
		printf("Elemento não está na lista\n");
	} else{
		NOLISTA* anterior = p->ant; //aqui eu to pegando a caixa anterior de p
		NOLISTA* proximo = p->prox; //aqui eu pego a caixa DEPOIS do q eu quero remover
		//printf("chegou\n");

		//anterior eh a nossa CAIXA
		//falta mudar pra quem aponta
		//printf("")
		anterior->prox = p->prox; // aqui eu faço aquele "pulo", excluindo o valor q quero tirar da lista
		//printf("chegou2\n");
		proximo->ant = p->ant; //aqui eu aponto o ultimo pro anterior à aquele q eu quero remover
		free(p);



	
	}


}



int main(){
	NOLISTA* cab;
	
	cab =(NOLISTA*) malloc(sizeof(NOLISTA));
	
	criar(cab);
	int escolha;
	
	/*printf("Digite 1 para inserir um elemento no inicio\n");
	printf("Digite 0 para sair\n");
	printf("Digite 2 para remover um item\n");
	scanf("%d",&escolha);
	*/
	while(1){
		printf("Digite 1 para inserir um elemento no inicio\n");
		printf("Digite 2 para remover um item\n");
		printf("Digite 3 para inserir um item na ordem\n");
		printf("Digite 0 para sair\n");
		scanf("%d",&escolha);


		if(escolha == 0){
			printf("Tchau\n");
			break;
		}

		if(escolha == 1){
			
			int k;

			printf("Qual valor deseja inserir?\n");

			scanf("%d",&k);

			insere1(cab,k);
			printf("----------------\n");
			imprimir(cab);
			printf("----------------\n");
			printf("Qual valor deseja retirar ?\n");

		}
		if(escolha == 2){
			int k1;

			printf("Qual valor deseja retirar ?\n");

			scanf("%d",&k1);

			retira(cab,k1);

			printf("----------------\n");
			imprimir(cab);
			printf("----------------\n");

		}
		if(escolha == 3){
			int k2;

			printf("Qual valor deseja inserir?\n");

			scanf("%d",&k2);

			insere_ord(cab,k2);

			printf("----------------\n");
			imprimir(cab);
			printf("----------------\n");



		}



	}





	free(cab);

	return 0;
}