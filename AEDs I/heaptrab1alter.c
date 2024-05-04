#include <stdio.h>
#include <stdlib.h>
#include <time.h>
/*
#define pai(i)  ((i - 1)/2)
#define esq(i)  (2*(i) + 1)
#define dir(i)  (2*(i) + 2)
*/
int pai(int i){
    return (i/2);

}
int esq(int i){
    return (2*i);
}
int dir(int i){
    return (2*i + 1);
}
int printvet(int vet[],int n){
    for(int i =0; i < n; ++i)
        printf("%d ",vet[i]);
    printf("\n");
}



void troca(int *v,int i,int j){
    int tmp = v[i];
    v[i] = v[j];
    v[j] = tmp;
}
void desce(int n,int *v,int i){
    int c = esq(i);
    while(c < n){
        int c2 = dir(i);
        if(c2 < n && v[c2] > v[c])
            c = c2;
        if(v[c] < v[i])
            break;
        troca(v,i,c);
    }


}

void sobeheap(int *v,int pos){
    int i;
    int j = pai(i);
    if(j >= 1){
        if(v[pos] > v[j]){
            //faz a subida
            int temp = v[i];
            v[i] = v[j];
            v[j] = temp;
            sobeheap(v,j);
        }
    }
}

void criaheap(int *v,int pos){
    for(int i =1;i < pos;++i)
        sobeheap(v,pos);
}


int hsort(int *v,int n){
    int i;
    //rearranja os elementos no vetor como em um heap
    for(i = n/2 - 1;i >=0;i--)
        desce(n,v,i);

    //remove os elementos, armazenado-os no final do vetor
    int k = n;
    for(int i =0;i < n;++i){
        printvet(v,n);
        troca(v,0,--k);
        desce(k,v,0);
    }


}


int insere(int *vet,int n,int new){
    vet = (int*) realloc(vet,n+1);
    vet[n] = new;
    n++;
    //sobeheap(vet,n);

    return n;


}

int excluir(int *vet,int n,int exclui){

    //diminui o tamanho do vetor
    troca(vet,n,exclui);

    vet =(int*) realloc(vet,n - 1);
    n--;

    desce(n,vet,0);

    return n;


}



int main(){
    int *vet;
    int n;
    int entrada;
    printf("Qual operação deseja realizar?\n");
    printf("Digite 1 para criar heap de máximo\n");
    printf("Digite 2 para inserir um novo elemento no Heap\n");
    printf("Digite 3 para remover um elemento do Heap\n");
    printf("Digigte 4 para remover um item e mudar sua prioridade\n");
    scanf("%d",&entrada);

    printf("Insira o tamanho do vetor\n");
    scanf("%d",&n);

    vet = (int*) malloc(n*sizeof(int));
    srand(time(NULL));
    for(int i =0 ; i < n;++i)
        vet[i] = rand() % 100;


    //printvet(vet,n);
    if(entrada == 1){
        for(int i = 1;i < n;i++)
            sobeheap(vet,i);

        printvet(vet,n);

    }
    else if(entrada == 2){
        int novo;
        printf("Insira um elemento novo\n");
        scanf("%d",&novo);

        n = insere(vet,n,novo);

        desce(n,vet,0);
        printvet(vet,n);

    }

    else if(entrada == 3){
        int k;
        scanf("%d",&k);
        int excluivar;
        n = excluir(vet,n,excluivar);
        //hsort(vet,n);
        printvet(vet,n);

    }

    free(vet);
    return 0;
}
