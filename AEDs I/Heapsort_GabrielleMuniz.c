#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

void desce_heap(int *vet, int pai, int t){
    int p = vet[pai], fil_esq = (pai*2)+1;;
    while(fil_esq <= t){
        if(fil_esq < t && vet[fil_esq] < vet[fil_esq+1])
            fil_esq++;
        if(p >= vet[fil_esq]){
            fil_esq = t+1;
        }else{
            vet[pai] = vet[fil_esq];
            pai = fil_esq;
            fil_esq = pai*2;
        }
    }
    vet[pai] = p;
}

void inserir(int *vetor, int nov_valor, int tam){
    tam++;
    vetor[tam] = nov_valor;
    desce_heap(vetor, nov_valor, tam);
    for(int i = 0; i < tam; i++)
        printf("%d ", vetor[i]);
}

void cria_heap(int *vetor, int tamanho){
    for(int k = (tamanho-1)/2; k >= 0; k--){
        desce_heap(vetor, k, tamanho-1);
    }
}

void heapsort(int *v, int tam){
    int t;
    for(int j = (tam-1)/2; j >= 0; j--)
        desce_heap(v, j, tam-1);
    
    for(int i = tam-1; tam >= 1; i--){
        t = v[0]; 
        v[0] = v[i]; 
        v[i] = t;

        desce_heap(v, 0, i-1);

        printf("Passo %d: ", tam-i);
        for(int g = 0; g < tam; g++)
            printf("%d ", v[g]);
        printf("\n");
    }
}

int main(){
    int n;
    // Definição do tamanho do heap pelo usuário
    printf("Insira o tamanho do heapsort: ");
    scanf("%d", &n);
    
    int heap[n];
    // Criação do heap
    printf("Insira os valores do heapsort: ");
    for(int i = 0; i < n; i++)
        scanf("%d", &heap[i]);
    printf("\n");

    // Apresentação do heap
    printf("Heap: [");
    for(int i = 0; i < n - 1; i++)
        printf("%d | ", heap[i]);
    printf("%d]", heap[n-1]);
    printf("\n");

    int menu, novo_valor, pos_rem, pos, nova_priori;
    do{
        printf("Escolha uma operacao do menu de acordo com o numero correspondente!\n\n");
        printf("1. Heapsort eh executado com seu passo a passo.\n2. Insira um novo elemento no Heap\n3. Remova um elemento do Heap.\n");
        printf("4. Insira uma posicao e uma nova prioridade (nessa ordem) para alterar a prioridade de um elemento\n\n");
        scanf("%d", &menu);

        switch(menu){
            case 1:
                heapsort(heap, n);
                break;
                //Não consegui corrigir erro no printf que acaba imprimindo mais valores do que o devido

            case 2: 
                printf("Qual elemento a ser inserido? ");
                scanf("%d", &novo_valor);
                inserir(heap, novo_valor, n);
                
                break;

            case 3:
                printf("Qual posicao deseja remover? ");
                scanf("%d", &pos_rem);
                heapsort(heap, n);
                for(int i = 0; i < n; i++){
                    if(heap[i] == pos_rem)
                        heap[i-1] = heap[i];
                }

                for(int j = 0; j < n-1; j++)
                    printf("%d ", heap[j]);

                break;

            case 4:
                printf("Insira a posicao e a nova prioridade (nesta ordem): ");
                scanf("%d%d", &pos, &nova_priori);
                cria_heap(heap, n);
                heap[pos-1] = nova_priori;
                
                heapsort(heap, n);
                
                break;
                // Retira o valor correto porém não consegui corrigir erro no printf que acaba imprimindo mais valores do que o devido
            default:
                printf("Por favor insira um numero valido!\n");
        }
    } while (menu < 1 || menu > 4);

    return 0;
}