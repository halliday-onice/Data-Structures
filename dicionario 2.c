#include <stdio.h>
#include <string.h>
#include <stdlib.h>


struct nodeAVL{
	char palavra[60];
	struct nodeAVL* pai;
	struct nodeAVL* esq;
	struct nodeAVL* dir;
	int altura;
	int fb; //fator de balanceamento
};


struct nodeRB{
	char palavra[60];
	char significado[200];
	struct nodeRB* pai;
	struct nodeRB* esq;
	struct nodeRB* dir;
	int cor; //1- vermelho 0-preto
	//dois ponteiros pra arvore AVL
	struct nodeAVL* antonimo;
	struct nodeAVL* sinonimo;
};




void inicializaAVL(struct nodeAVL* v){
	v->esq = NULL;
	v->dir = NULL;
	v->fb = 10;
	v->altura = 1;

}



struct nodeAVL* alocaAVL(){
	return (struct nodeAVL*) malloc(sizeof(struct nodeAVL));

}


struct nodeAVL* buscaAVL(struct nodeAVL* root,char word[60]){
	//struct nodeAVL* aux;

	if(root == NULL) //se raiz for nula
		return NULL;

	if(strcmp(root->palavra,word) == 0) //se for ja a raiz
		return root;

	if(strcmp(root->palavra,word) < 0){ //se o no estiver a direita, vou seguindo
		return buscaAVL(root->dir,word);
	} else{ // se no a esquerda
		return buscaAVL(root->esq,word);
	}

	
}

int Altura(struct nodeAVL* v){//calcula a altura de um no
	int alt_esq = 0;
	int alt_dir = 0;

	if(v->esq)
		alt_esq = Altura(v->esq);
	if(v->dir)
		alt_dir = Altura(v->dir);

	return alt_dir > alt_esq ? ++alt_dir : ++alt_esq;
}

//getBalance
int fatorB(struct nodeAVL* node){
	int bf = 0;

	if(node->esq)
		bf += Altura(node->esq);
	if(node->dir)
		bf -= Altura(node->dir);

	return bf;
}

//recebe um no e diz qual eh o tamanho da maior subarvore
int Max(struct nodeAVL* gauche,struct nodeAVL* droite ){
	int value_subesq,value_subdir;

	if(gauche != NULL)
		value_subesq = gauche->altura;
	else
		value_subesq = 0;

	if(droite!= NULL){
		value_subdir = droite->altura;
		//printf("%d\n",value_subdir);
	}else{
		value_subdir = 0;
	}

	//para retornar a arvore maior
	if(value_subesq > value_subdir)
		return value_subesq;
	else
		return value_subdir;

}


struct nodeAVL* RR_AVL(struct nodeAVL* no){
	//tudo q for esq vira dir
	struct nodeAVL* aux = no->esq;
	struct nodeAVL* aux2 = aux->dir;

	aux->dir = no;
	//aux2->dir = aux;
	aux->pai =no->pai;

	if(no->pai != NULL){
		if(no->pai->esq == no){
			no->pai->esq = aux;
		} else {
			no->pai->dir= aux;
		}
	}
	no->pai = aux;
	no->esq = aux2;

	if(aux2 != NULL){
		aux2->pai = no;
	}
	struct nodeAVL* atualizafb = no;

	while(atualizafb!= NULL){
		atualizafb->fb = fatorB(atualizafb);
		atualizafb = atualizafb->pai;


	} 

	return aux;


	
}

struct nodeAVL* LL_AVL(struct nodeAVL* no){
	struct nodeAVL* aux = no->dir;
	struct nodeAVL* aux2 = aux->esq;


	aux->esq = no;
	//aux2->dir = aux;
	aux->pai =no->pai;


	if(no->pai != NULL){
		if(no->pai->dir == no){
			no->pai->dir = aux;
		} else {
			no->pai->esq = aux;
		}
	}
	no->pai = aux;
	no->dir = aux2;

	if(aux2 != NULL){
		aux2->pai = no;
	} 

	struct nodeAVL* atualizafb = no;

	while(atualizafb!= NULL){
		atualizafb->fb = fatorB(atualizafb);
		atualizafb = atualizafb->pai;


	} 


	return aux;
	
}

struct nodeAVL* RL_AVL(struct nodeAVL* no){
	struct nodeAVL* aux = no;
	struct nodeAVL* aux2 = aux->dir;
	struct nodeAVL* aux3 = aux2->esq;

	aux = RR_AVL(no->dir);

	aux = LL_AVL(aux->pai);

	if(aux == NULL)
		no = aux;
	

	return aux;


}

struct nodeAVL* LR_AVL(struct nodeAVL* no){
	struct nodeAVL* aux = no;
	struct nodeAVL* aux2 = aux->esq;
	struct nodeAVL* aux3 = aux2->dir;
	
	aux = LL_AVL(no->esq);

	aux = RR_AVL(aux->pai);

	if(aux == NULL)
		no = aux;
	


	return aux;
}


struct nodeAVL* InsereAVL(struct nodeAVL* no, char newword[60]){
	
	//puts("entrou");
	//printf("NEW WORD: %s\n",newword);
	struct nodeAVL* aux = no;
	struct nodeAVL* aux2 = NULL;
	//puts("AAAAAAAAAAAAAAAAAAAAAA");
	//printf("A: %s\n",no->palavra);
	//puts("entrou");
	if(aux->fb == 10){
		//puts("entrou if");
		aux->fb = 0;
		aux->altura = 1;
		//printf("Adicionado raiz\n");
		strcpy(no->palavra,newword);

		return no;
	}
	else { //se entrar aqui eh porque ja possui raiz
		//aloca espaco na memoria pro novo no
		//printf("NAO EH RAIZ\n");
		struct nodeAVL* new = alocaAVL();
		new->esq = NULL;
		new->dir = NULL;
		new->fb = 0;//no folha o fb eh zero 
		new->altura = 1;
		
		strcpy(new->palavra,newword);
		
		while(aux != NULL){
			
			aux2 = aux;
			//printf("aux2 dentro do while AVL:%s\n");
			//printf("Entrou no while Insercao AVL\n");
			if(strcmp(new->palavra,aux2->palavra) < 0){
				aux = aux->esq;
				//puts("acr");
			} else {
				aux = aux->dir;
				//puts("asks");
			}
			
		}
		new->pai = aux2;
		//puts("");
		//printf("NEW->PAI:%s\n",new->pai->palavra);
		//puts("");
		//aqui eh pra ver se vou adicionar na sub arvore esquerda ou direita
		if(strcmp(new->palavra,aux2->palavra) > 0){
			aux2->dir = new;
		} else {
			aux2->esq = new;
		}
		//ATE A 206 ESTA CERTO 
		//printf("%s\n",aux2->palavra);
		
		//puts("antes de atualizar");
		//preciso verificar a altura e o fator de balanceamento de todo mundo ate chegar a raiz
		struct nodeAVL* auxiliar = new;
	 	while(auxiliar != NULL){
	 		//puts("entrou no while pra consertar");
		 	auxiliar->altura = Max(auxiliar->esq,auxiliar->dir) + 1; //altura do no inserido conta como 1, por isso o mais 1
		 	//puts("recalculo o fb");
		 	//printf("AUXILIAR->ALTURA:%d\n",auxiliar->altura);
		 	//int factorba;

		 	auxiliar->fb = fatorB(auxiliar);
		 	//printf("AUXILIAR->FB: %d\n",auxiliar->fb);
		 	//printf("AUXILIARY ->PALAVRA: %s\n",auxiliar->palavra);
		 	//printf("FACTOR BALANCEAMENTO: %d\n",auxiliar->fb);
		 	if(auxiliar->fb != 0 && auxiliar->fb != -1 && auxiliar->fb != 1){
		 		//puts("ALOUY ALOU ALOU");
		 		break;
		 	}
		 	auxiliar = auxiliar->pai;
		 	//puts("ALOU AOUA ALAI");
		 	

	 	}
	 	//puts("OQ SJAAAAAAAAAAAAAAAAA");

	 	
	 	struct nodeAVL* aux3 = auxiliar;
	 	if(aux3!= NULL){ //se o no for nulo,nao vai conseguir pegar o FB
		 	if(aux3->fb == -2 && aux3->dir->fb != 1){
		 		//puts("ANTES DA LL");
		 		aux3 = LL_AVL(aux3);
		 		//puts("DEPOIS DO LL");
		 		//puts("");
		 		//printf("aux3->palavra:%s\n",aux3->palavra);

		 		

		 	} else if(aux3->fb == -2){
		 		//puts("ANTES DO RL");
		 		aux3 = RL_AVL(aux3);
		 		//puts("DEPOIS DO RL");

		 	}

		 	if(aux3->fb == 2 && aux3->esq->fb != -1){
		 		//puts("ANTES DO RR");
		 		//printf("no->dir:%s\n",aux3->dir->palavra);
		 		aux3 = RR_AVL(aux3);
		 		//puts("DEPOIS DO RR");

		 		

		 	} else if(aux3->fb == 2){
		 		//puts("ANTES DO LR");
		 		aux3 = LR_AVL(aux3);
		 		//puts("DEPOIS DO LR");

		 	}

		 	if(aux3->pai == NULL)
		 		no = aux3;

		}
		 	
		 
		return no;

	

	}
	


}//fim insereAVL

void imprimeAVL(struct nodeAVL* root){
	if(root){
		puts("++++++++++++++++++++++");
		printf("%s\n",root->palavra);
		imprimeAVL(root->esq);
		imprimeAVL(root->dir);


	} 



}




// Funcoes da arvore RUBRO NEGRA
// 
// 
// 
// 
// 
// 

void inicializaRB(struct nodeRB* v){
	//puts("inicio RB");
	v->pai = NULL;
	v->esq = NULL;
	v->dir = NULL;
	v->cor = 1;//inicializa sempre como vermelho
	
	v->antonimo = alocaAVL();
	v->sinonimo = alocaAVL();
	inicializaAVL(v->antonimo);
	inicializaAVL(v->sinonimo);

	

}

struct nodeRB* alocaRB(){
	return (struct nodeRB*) malloc(sizeof(struct nodeRB));
 }

struct nodeRB* LL_RB(struct nodeRB* arv){
	struct nodeRB * aux;

	aux = arv->dir;
	

	if(arv->pai != NULL){ //olho se nao eh raiz
		//arv->pai = NULL;
		//printf("Chegou dentro do arv->pai != NULL\n");
	 
		if(arv == arv->pai->esq)
			arv->pai->esq = aux;
		else
			arv->pai->dir = aux;
	}
	// control + / comenta varias linhas
	//printf("arv->esq->palavra:%s\n",aux->esq->palavra);
	 arv->dir = aux->esq;
	 // if(aux->esq != NULL)
	 // 	aux->esq->pai = arv;
	 aux->esq = arv;
	 aux->pai = arv->pai;
	 arv->pai = aux;
	 arv = aux;
	 
	 return arv;
}

struct nodeRB* RR_RB(struct nodeRB* arv){
	//puts("entrou RR");
	struct nodeRB * aux;

	
	
	aux = arv->esq;
	//printf("%s\n",aux->dir->palavra);

	if(aux->dir != NULL)
		aux->dir->pai = arv;
	//puts("if");
	
	//printf("print antes do if RR\n");

	if(arv->pai != NULL){
		if(arv == arv->pai->esq)
			arv->pai->esq = aux;
		else
			arv->pai->dir = aux;
	}
	//printf("print dps do if RR\n");
	//printf("arv->pai :%p\n",arv->pai);

	arv->esq = aux->dir;
	aux->dir = arv;
	aux->pai = arv->pai;
	arv->pai = aux;
	arv = aux; 
	return arv;
}


struct nodeRB* Insere_fix(struct nodeRB* arv,struct nodeRB* v){
	struct nodeRB* u; //u de uncle(tio)
	//printf("chegou\n");
	while(v->pai->cor == 1){//pai na subarvore esquerda vermelho
		//printf("Entrou no while\n");
		//printf("v->palavara insere_fix:%s\n",v->palavra);
		if(v->pai == v->pai->pai->esq){ //to verificando se o pai ta na esquerda
			u = v->pai->pai->dir;//pego o tio q nesse caso vai ta na direita
			//printf("chegou no tio a direita\n");
			if(u == NULL){//estamos vendo se o tio for nulo(nao existe)
				
				u = alocaRB(u);
				u->cor = 0;
				//printf("sem tio\n");
			} 
			if(u->cor == 1){//pai v e tio v só mudo cores
				//printf("chegou dentro dentro do u->cor == 1\n"); 
				//printf("v->pai->pai->cor:%d \n",v->pai->pai->cor);
				v->pai->cor = 0;
				u->cor = 0;
				v->pai->pai->cor = 1;
				//printf("v->pai->pai->cor:%d \n",v->pai->pai->cor);
				//v =  v->pai->pai;
				//printf("")
				
			}
			else{ //pai v tio p
				//puts("bbbbbbbbbbb");
				if(v == v->pai->dir){


					v = v->pai;
					v = LL_RB(v);
					//printf("if v == v->pai->dir:%s\n",v->palavra);
					v = v->esq;
					//printf("if v == v->pai->dir 2:%s\n",v->palavra);
				}

				//puts("chegou no else");
				//printf("v->pai->pai :%s",v->pai->palavra);
				v = RR_RB(v->pai->pai);
				//printf("	QUEM EH O V->PAI : %s\n",v->pai->palavra);

				//printf("vish kct\n");
				v->cor = 0;
				v->dir->cor = 1;
				//printf("v->dir->palavra %s\n",v->dir->palavra);
				if(v->pai == NULL){
					arv = v;
					arv->cor = 0;
					break;
				}
			}

		} else{//pai na subarvore esquerda
			//printf("chegou no tio a esquerda\n");
			u = v->pai->pai->esq;
			if(u == NULL){
				u = alocaRB();
				u->cor = 0;
				//agr nao vai mais dar falha de segmentacao
				//vai pular pro tio preto

			}
			//printf("%p\n",u);
			//pai vermelho e tio v so mudo cores
			if(u->cor == 1){
				//printf("Chegou no tio vermelho\n");
				v->pai->cor = 0;
				u->cor = 0;
				v->pai->pai->cor = 1;
			} else{
				//printf("Chgeou no tio preto\n");
				if(v == v->pai->esq){
					v = v->pai;
					v = RR_RB(v);
					//printf("v->palavra:%s\n",v->palavra);
					v = v->dir;

				}
				//printf("Antes do LL\n");
				v = LL_RB(v->pai->pai);
				//printf("Logo dps do LL\n");
				if(v->pai != NULL)
					v->cor = 0; //mudando a cor do v p V
				//printf("v->pai->cor = 0\n");
				v->esq->cor = 1;

				if(v->pai == NULL){ //to verificando se eh raiz
					arv = v; // to atualizando a raiz
					arv->cor = 0;
					break;

					//printf("v->pai->pai->cor\n");
				}

			}

		}

	}
	arv->cor = 0;
	return arv; 


}

//raiz e oq eu quero inserir
struct nodeRB* InsereRB(struct nodeRB* arv,struct nodeRB* new){

	
	
	//entao aqui eh a raiz
	struct nodeRB* aux = arv;
	struct nodeRB* aux2 = NULL; //referencia o pai

	while(aux!= NULL){
		aux2 = aux;
		//printf("entrou no while do INSERERB\n");
		//printf("pai: %s\n",new->pai->palavra);
		if(strcmp(new->palavra, aux2->palavra) < 0){
			//printf("entrou no strcmp\n");
			aux = aux->esq;
		} else{
			aux = aux->dir;
			//printf("entrou no else strcmp\n");
		}

	}

	//printf("saiu do while\n");
	new->pai = aux2;
	if(aux2 == NULL){
		arv = new;

	} else if(strcmp(new->palavra,aux2->palavra) > 0){
		//printf("entrou\n");
		aux2->dir = new;
	}
	else{
		//printf("entrou\n");
		aux2->esq = new;
	}

	new->esq = NULL;
	new->dir = NULL;
	new->cor = 1; //vermelho
	//printf("antes do Insere_fix:%s\n",new->palavra);
	arv = Insere_fix(arv,new);

	//printf("Dps do insere_fix\n");


	return arv;
	



}

struct nodeRB* buscaItemRB(struct nodeRB* root, char word[60]){
	struct nodeRB* aux = root;
	while(aux!= NULL){ //se raiz for nula
			
		if(strcmp(aux->palavra,word)== 0) //se for a palavra procurada
		{	
			printf("Palavra: %s\n",aux->palavra);
			printf("significado:%s\n",aux->significado);
			if(aux->antonimo != NULL){
				printf("Antoninimo:\n");
				imprimeAVL(aux->antonimo);
			}
			if(aux->sinonimo != NULL){
				printf("Sinonimo:\n");
				imprimeAVL(aux->sinonimo);
			
			}
			return aux;
		}

		if(strcmp(aux->palavra,word) < 0){ //se o no estiver a direita, vou seguindo

			aux = aux->dir;

		} else{ // se no a esquerda
			aux = aux->esq;
			//return buscaItemRB(root->esq,word);
		}
		return NULL;


	}
	


}
//arv eh a raiz
//substitui a raiz no no u e coloca no no z
struct nodeRB* trocaRaizRB(struct nodeRB* arv, struct nodeRB* u, struct nodeRB* v){// o u eh oq eu quero botar o v no u
	//struct nodeRB* aux;
	/* troca os pais de um no v*/
	if(u->pai == NULL){// pai do no apontar pro sucessor
		arv = v;
	} else if(u == u->pai->esq){
		u->pai->esq = v;
	} else{
		u->pai->dir = v;

	}
	v->pai = u->pai; //faz o pai do sucessor ser o pai do no
	return arv;
}
// recebe struct nodeRB* aux2
struct nodeRB* RemoveRB_fix(struct nodeRB* arv,struct nodeRB* v){
	struct nodeRB* aux;
	while(v != arv && v->cor == 0){
		if(v == v->pai->esq){ //else na linha 335
			aux = v->pai->dir;
			if(aux->cor == 1){//caso 3.1 irmao Vermelho
				/* muda cor irmao e pai e faz LL no pai*/
				aux->cor = 0;
				v->pai->cor = 1;
				v = LL_RB(v->pai);//se nao for isso testar arv


			}
			if(aux->esq->cor == 0 && aux->dir->cor == 0){//caso 3.2
				/*irmão e seus filhos sao pretos
				retirar um preto do no e um do irmao,e mudamos o irmao pra vermelho */
				aux->cor = 1;
				aux = aux->pai;

			} else if(aux->dir->cor == 0){ //caso 3.3
				aux->esq->cor = 0;
				aux->cor = 1;
				aux = RR_RB(aux);
				//linha16 slide
				aux = v->pai->dir;
				aux->cor = v->pai->cor;
				v->pai->cor = 0;

			}
			aux->dir->cor = 0;
			aux = LL_RB(v->pai);
			v = arv;

		} else {
			aux = v->pai->esq;
			if(aux->cor == 1){//caso 3.1 irmao Vermelho
				/* muda cor irmao e pai e faz LL no pai*/
				aux->cor = 0;
				v->pai->cor = 1;
				v = LL_RB(v->pai);


			}
			if(aux->dir->cor == 0 && aux->esq->cor == 0){//caso 3.2
				/*irmão e seus filhos sao pretos
				retirar um preto do no e um do irmao,e mudamos o irmao pra vermelho */
				aux->cor = 1;
				aux = aux->pai;

			} else if(aux->dir->esq == 0){ //caso 3.3
				aux->dir->cor = 0;
				aux->cor = 1;
				aux = RR_RB(aux);
				//linha16 slide
				aux = v->pai->esq;
				aux->cor = v->pai->cor;
				v->pai->cor = 0;

			}
			aux->dir->cor = 0;
			aux = LL_RB(v->pai);
			v = arv;
			v->cor = 0;//linha 23

		}
	}
	return v;


}


struct nodeRB* RemoveRB(struct nodeRB* arv, struct nodeRB* v){
	struct nodeRB* aux = v;
	int cor_aux = aux->cor; // 1- V, 0- P


	struct nodeRB* aux2; 
	//printf("antes de ver se eh no folha:%s\n",aux->palavra);
	//slide 04
	//verificar se eh um no folha, ou seja se nao tem filho a esq nem a direita
	if(aux->esq == NULL && aux->dir == NULL){
		//v->pai NULL tem q apont
		//v->pai->esq NULL e
		//puts("aaaa");

		if( aux == aux->pai->esq ){//se essa condicao for satisfeita quer dizer q o no q querems remover esta na esq
			//puts("bbbb");
			aux->pai->esq = NULL;
			aux->pai = NULL;
			
			free(aux);

		} else if(aux == aux->pai->dir){//ta certo
			//printf("bbbb\n");
			aux->pai->dir = NULL;
			aux->pai = NULL;
			//printf("chegou subarvore dir\n");
			
			free(aux);
		}

		
	}
	else if(aux->esq == NULL){ //no vermelho e estamos vendo se ele tem um filho
		aux2 = v->dir;
		aux2 = trocaRaizRB(arv,v,aux2);
		//printf("dps do troca raiz: %s\n",aux2->palavra); //isso aqui ele me da o b
		aux2->cor = 0;
		aux->pai->dir = NULL;
		aux->pai = NULL;

		free(aux);


	} else {//se entrar nesse else eh pq tem 2 filhos

		
		//A,proFputs("Entrou no else de dois filhos");
		struct nodeRB* antecessor;
		struct nodeRB* percorrearv = aux->esq; //estou pegendo o antecessor, ai 
		//preciso comecar a percorrer a subarvore a esquerda , toda a direita
		if(percorrearv->dir == NULL){//nesse if to vendo se o antecessor ja nao eh o filho a esquerda
			//nao entra no while
			antecessor = percorrearv;
			//printf("antecessor:%s\n",antecessor->palavra);
		} else{
			while(percorrearv->dir != NULL){//to percorrendo toda a arv a direita
				percorrearv = percorrearv->dir;
			}//sai do while quando eu pegar o antecessor, por isso o antecessor = percorrearv
			antecessor = percorrearv;
		}
		cor_aux = antecessor->cor;

		if(antecessor->esq != NULL)//so vai pegar aux2 como antecessor a esq se o ant a esq existir
			aux2 = antecessor->esq;// se der errado, mudar pra antecessor->dir
		
		printf("%s\n",antecessor->palavra);
		//if()
		//free(aux2);
		//y  antecessor sempre
		//linha 13 do slide RB_Delete(T,v)
		/*Nesse if,to verificando se o antecessor pai ja eh o proprio v */
		if(antecessor->esq !=NULL){
			if(antecessor->pai == v){//eh o proprio filho do no
				aux2->pai = antecessor;//se nao for v eh antecessor
			}
			else{ //aux2 eh o x
				aux2 = trocaRaizRB(arv,aux,aux2);
				antecessor->esq = v->esq;
				antecessor->esq->pai = antecessor;
				//printf("aux2:%s",aux2->palavra);
				//free(aux2);

			}
		}


		//printf("aux :%s\n",aux->palavra);
		aux2 = aux->dir;//
		struct nodeRB* aux3 = trocaRaizRB(arv,v,antecessor);
		//printf("aux dps trocaraiz:%s\n",aux3->palavra);
		
		
		//printf("antecessor:%s\n",antecessor->palavra);
		//printf("antecessor->pai:%s\n",antecessor->pai->palavra);
		antecessor->dir = v->dir;
		antecessor->dir->pai = antecessor;
		antecessor->cor = v->cor;
		v->pai = NULL;

		//if(antecessor != antecessor->pai)
		//	antecessor->esq = v->esq;
		//antecessor = LL_RB(antecessor);
		//consertar pai do d
		//printf("aux")

		//printf("antecessor dps do LL:%s\n",antecessor->dir->palavra);

		//printf("ant->dir:%s\n",antecessor->dir->palavra);
		//printf("ant->pai:%s\n",antecessor->dir->pai->palavra);

		free(aux);








	}
	/*aqui estou verificando se eh duplo preto ou nao */
	if(cor_aux == 0){
		//aux = RemoveRB_fix(arv,v);
		//printf("%s\n",aux->palavra);
	}



}

struct nodeRB* buscaNoRB(struct nodeRB* root, char v[60]){
	struct nodeRB* auxiliar = root;
	if(strcmp(auxiliar->palavra,v) == 0)
		return root;

	while(auxiliar != NULL){
		// if(auxiliar->palavra == NULL)
		// 	return NULL;
	
		if(strcmp(auxiliar->palavra,v)== 0)
			return auxiliar;
		else if(strcmp(auxiliar->palavra,v) < 0){
			auxiliar = auxiliar->dir;
		} else {
			auxiliar = auxiliar->esq;
		}
	
	}

	//printf("")
	
	// 	return root;
	// }

	return NULL;


}


int main(){
	int control = 1;
	int option;

	//inicializa a raiz com a cor preta
	struct nodeRB* raiz = alocaRB();
	int seforraiz = 0;
	raiz->cor = 0;
	struct nodeRB* no;
	struct nodeRB* target = alocaRB();

	//struct nodeAVL* raizAVL = alocaAVL();
	
	while(control){
		printf("+++++++++++++++++++\n");
		printf("Escolha uma opcao:\n");
		printf("Fim: 0\n");
		printf("Inserir uma palavra no dicionario com seu significado(ARN): 1\n");
		printf("Para remover uma palavra digite 2:\n");
		printf("Para fazer um busca de uma palavra 3:\n");
		printf("Para cadastrar um antonimo:4\n");
		scanf("%d",&option);
		switch(option){
			case 0:
				control = 0;
				break;
			case 1:
				no = alocaRB();
				inicializaRB(no);
				char word[60];
				char significadinho[200];
				puts("Digite a palavra {espaço} significado");
				scanf("%s",word);
				scanf("%[^\n]",significadinho);

				strcpy(no->palavra,word);
				strcpy(no->significado,significadinho);

				if(seforraiz == 0){
					raiz->cor = 0;
					raiz = no;
					printf("Palavra %s inserida\n",no->palavra);
				} else{
					raiz = InsereRB(raiz,no);
					printf("Palavra %s inserida\n",no->palavra);
				}

				break;
			case 2:
				puts("");
				//struct nodeRB* aux1 = alocaRB();
				struct nodeRB* aux2;
				aux2 = alocaRB();
				//buscaItemRB;
				char wordDelete[60];
				printf("Qual palavra quer remover?\n");

				scanf("%s",wordDelete);
				//strcpy(aux2->palavra,wordDelete);
			
				target = buscaNoRB(raiz,wordDelete);
				puts("aaaaa");
				//printf("");
				printf("TARGET: %s\n",target->palavra);
				//printf("AAAA: %s\n",buscaNoRB(no,wordDelete)->palavra);
				
				//printf("target:%s\n",aux2->palavra);
				if(no != NULL){
					puts("entrou no remover");
					//printf("%s\n",raiz->palavra);
					raiz = RemoveRB(raiz,target);
					//printf("Palavra %s removida\n",no->palavra);
				} 
				break;

			case 3:
				puts("");
				char wordP[60];
				printf("Qual palavra quer buscar?\n");

				scanf("%s",wordP);
				target = buscaNoRB(raiz,wordP);

				


				printf("Palavra:%s\n",target->palavra);
				printf("Significado:%s\n",target->significado);

				if(target->sinonimo != NULL){
					printf("Sinonimo :%s\n",target->sinonimo->palavra);
				}
				if(target->antonimo != NULL){
					printf("Antonimo: %s\n",target->antonimo->palavra);
				}

				break;
			case 4:
				puts("");
				printf("Digite duas palavras que ja estão no sistema: ");
				struct nodeRB* aux1 = alocaRB();
				struct nodeRB* aux3 = alocaRB();
				char w1[60],w2[60];
				scanf("%s %s",w1,w2);
				aux1 = buscaNoRB(raiz,w1);
				aux3 = buscaNoRB(raiz,w2);
				printf("aux1->Palavra:%s\n",aux1->palavra);
				printf("aux3->Palavra:%s\n",aux3->palavra);
				aux1 = buscaItemRB(raiz,w1);
				aux3 = buscaItemRB(raiz,w1);

				if( (aux1 != NULL && aux3 != NULL)){
					aux1->antonimo = InsereAVL(aux1->antonimo,w1);
					aux3->antonimo = InsereAVL(aux3->antonimo,w2);

					printf("Os antanimos foram cadastrados\n");
				} else{
					printf("As palavras nao estao no sistema\n");
				}
				//pesquisa rn e se ambas estiverem cadastradas, faz a insercao na AVL
				break;

			// case 5:
			// 	puts("");
			// 	printf("Digite duas palavras que ja estão no sistema: ");
			// 	struct nodeRB* aux5 = alocaRB();
			// 	struct nodeRB* aux6 = alocaRB();
			// 	break;
				
				










			default:
				printf("ERRO digite um numero valido:\n");
				break;

				


				











		}
	}

	

// 	//meu cara inicial sempre
// 	//struct nodeRB *new = (struct nodeRB*)malloc(sizeof(struct nodeRB));
// 	//inicializaRB(new);


// 	struct nodeRB* raiz = alocaRB();
// 	inicializaRB(raiz);
// 	raiz->cor = 0;//preto
// 	//printf("raiz->pai: %p\n",raiz->pai);





// 	struct nodeRB* no = alocaRB();
// 	inicializaRB(no);
// 	strcpy(no->palavra,"a");
// 	no->cor = 1;

	
	

// 	// //raiz = no;

// 	// //puts("d");
	

	

// 	struct nodeRB* no1  = alocaRB();
// 	inicializaRB(no1);
// 	strcpy(no1->palavra,"c");
// 	no1->cor = 1;
// 	no1->palavra;




// 	struct nodeRB* no2  = alocaRB();
// 	inicializaRB(no2);
// 	strcpy(no2->palavra,"f");
// 	no2->cor = 0;


// 	struct nodeRB* no3 = alocaRB();
// 	inicializaRB(no3);
// 	strcpy(no3->palavra,"b");
// 	no3->cor = 1;


// 	struct nodeRB* no4 = alocaRB();
// 	inicializaRB(no4);
// 	strcpy(no4->palavra,"e");
// 	no4->cor = 1;
	

// 	struct nodeRB* no5 = alocaRB();
// 	inicializaRB(no5);
// 	strcpy(no5->palavra,"d");
// 	no5->cor = 0;

// 	raiz = no2;

// 	raiz = InsereRB(raiz,no4);
// 	raiz = InsereRB(raiz,no5);
// 	raiz = InsereRB(raiz,no1);


// // 
// // 
// // TESTE COM A ARVORE AVL
// // 
// // 
// // 
// // 
// 	no2->sinonimo = InsereAVL(no2->sinonimo,"duende");
// 	no2->sinonimo = InsereAVL(no2->sinonimo,"funda");
// 	no2->sinonimo = InsereAVL(no2->sinonimo,"espacamento");
// 	//coṕia no2->sinonimo = InsereAVL(no2->sinonimo,"circulo");
// 	//testar inserir mais duas ou tres palavras
// 	char significadono2[200] = "opa lele oh lala";
// 	strcpy(no2->significado,significadono2);
// 	no2= buscaItemRB(no2,"f");

// // 
// // TESTE AVL
// // 
// // 


// 	// puts("");
// 	// printf("pai da raiz: %s\n",no2->sinonimo->pai->palavra);
// 	// printf("RAIZ : %s\n",no2->sinonimo->palavra);
// 	// printf("fb da raiz: %d\n",no2->sinonimo->fb);
// 	// //printf("filho esq ciruculo: %s\n",no2->sinonimo->esq->palavra);
// 	// //printf("filho dir circulo: %s\n",no2->sinonimo->dir->palavra);
	
// 	// if(no2->sinonimo->esq != NULL){
// 	// 	printf("filho esq da raiz:%s\n",no2->sinonimo->esq->palavra);
// 	// 	printf("fb filho esq da raiz: %d\n",no2->sinonimo->esq->fb);
// 	// }
// 	// if(no2->sinonimo->dir != NULL){
// 	// 	printf("filho dir da raiz:%s\n",no2->sinonimo->dir->palavra);
// 	// 	printf("fb filho dir da raiz: %d\n",no2->sinonimo->dir->fb);
// 	// }
// 	// printf("\n");

// // 
// // TESTE AVL
// // 
// // 

	

	


	

	

	
// 	// //printf("raiz->pai: %p\n",raiz->pai);
// 	// //printf("raiz:%s\n",raiz->palavra);
// 	// raiz = InsereRB(raiz,no5);
// 	// //puts("d");
// 	// //printf("raiz->pai: %p\n",raiz->pai);
// 	// //printf("raiz:%s\n",raiz->palavra);
	
// 	// raiz = InsereRB(raiz,no1);
// 	// //puts("c");

// 	// raiz = InsereRB(raiz,no3);
// 	// //puts("b");
// 	// raiz = InsereRB(raiz,no);
// 	//puts("a");
	
	
// 	//raiz = RemoveRB(raiz,no5);

// 	// printf("%s\n",raiz->palavra);
// 	// printf("%s\n",no1->palavra);
// 	// printf("%s\n",no2->palavra);

// 	/* TO DO
// 	Fazer um caso quando o antecessor tiver filhos
// 	*/

	



// 	// printf("pai do a: %s\n",no->pai->palavra);
// 	// printf("cor do a: %d\n",no->cor);
// 	// //printf("filho esq da raiz: %s\n",raiz->esq->palavra);
// 	// //printf("filho dir a: %s\n",no->dir->palavra);
	
// 	// if(no->esq != NULL)
// 	// 	printf("filho esq do a:%s\n",no->esq->palavra);
// 	// if(no->dir != NULL)
// 	// 	printf("filho dir do a:%s\n",no->dir->palavra);
// 	// printf("\n");
	
// 	// printf("pai do b: %s\n",no3->pai->palavra);
// 	// printf("cor do b: %d\n",no3->cor);

// 	// //printf("filho esq do b: %s\n",no1->esq->palavra);
// 	// //printf("filho dir do b: %s\n",no1->dir->palavra);

// 	// if(no3->esq != NULL)
// 	// 	printf("filho esq do b:%s\n",no3->esq->palavra);
// 	// if(no3->dir != NULL)
// 	// 	printf("filho dir do b:%s\n",no3->dir->palavra);
// 	// printf("\n");

// 	// printf("pai do c: %s\n",no1->pai->palavra);
// 	// printf("cor do c: %d\n",no1->cor);
// 	// if(no1->esq != NULL)
// 	// 	printf("filho esq do c:%s\n",no1->esq->palavra);
// 	// if(no1->dir != NULL)
// 	// 	printf("filho dir do c:%s\n",no1->dir->palavra);
// 	// printf("\n");
// 	// printf("\n");

// 	// printf("pai do d: %s\n",no5->pai->palavra);
// 	// printf("cor do d: %d\n",no5->cor);
// 	// if(no5->esq != NULL)
// 	// 	printf("filho esq do d:%s\n",no5->esq->palavra);
// 	// if(no5->dir != NULL)
// 	// 	printf("filho dir do d:%s\n",no5->dir->palavra);
// 	// printf("\n");
// 	// printf("\n");

// 	// printf("pai do e: %s\n",no4->pai->palavra);
// 	// printf("cor do e: %d\n",no4->cor);
// 	// if(no4->esq != NULL)
// 	// 	printf("filho esq do e:%s\n",no4->esq->palavra);
// 	// if(no4->dir != NULL)
// 	// 	printf("filho dir do e:%s\n",no4->dir->palavra);
// 	// printf("\n");
// 	// printf("\n");

// 	// printf("pai do f: %s\n",no2->pai->palavra);
// 	// printf("cor do f: %d\n",no2->cor);
// 	// if(no2->esq != NULL)
// 	// 	printf("filho esq do f:%s\n",no2->esq->palavra);
// 	// if(no2->dir != NULL)
// 	// 	printf("filho dir do f:%s\n",no2->dir->palavra);
// 	// printf("\n");
// 	// printf("\n");






	




//
// 	
// AQUI ESTA FUNCIONANDO TODAS AS INSERCOES 
//  
// 
// 
//
//
	return 0;
}