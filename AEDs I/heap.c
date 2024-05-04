#include <stdio.h>
#include <stdlib.h>
#include <time.h>


int father(int i)
{
	return i/2;
}

int left(int i)
{
	return 2*i;
}

int right(int i)
{
	return 2*i + 1;
}

void printvector(int vector[], int size)
{
	//prints the vector 
	//receives a vector and its size

	for(int i =0; i < size; i++)
		printf("%d ",vector[i]);
	printf("\n");
	
}

void ShiftHeapUp(int *vectorHeap,int index)
{
	int tmpIndex = father(index); // tempIndex stands for the index of father node of the element that has been altered
	// store in a variable the father of the ACTUAL node we're a analyse

	if(tmpIndex >= 1){
		//then it is inside the Heap
		if(vectorHeap[index] > vectorHeap[tmpIndex]){
			//if the heap from the son is bigger than the father's one
			// I must enphasize that here, heap means priority 
			// we must change
			int temp = vectorHeap[index];
			vectorHeap[index] = vectorHeap[tmpIndex];
			vectorHeap[index] = temp;
			ShiftHeapUp(vectorHeap,tmpIndex); // call recursivily until the root

		}
	}




}

void Swap(int *a,int *b){
	int temp = *b;
	*b = *a;
	*a = temp;
}


void ShiftHeapDown(int *vectorHeap, int index, int n)
{	//index eh o indice do elemento que tem que descer
	//receives the heap, the index in wich we want to go down and the size 
	// First things first we must discover the wich son is greater
	int l = left(index);
	int r = right(index);

	int bigger = index;

	//printf("left: %d\n",vectorHeap[l]);
	//printf("right: %d\n",vectorHeap[r]);
	//printf("Bigger: %d\n",vectorHeap[bigger]);


	if(l < n && vectorHeap[l] > vectorHeap[index])
		bigger = l;
	if(r < n && vectorHeap[r] > vectorHeap[index])
		bigger = r;
	//printf("Bigger: %d\n",bigger);
	if(bigger != index){
		// we must change the priority
		Swap(&vectorHeap[index],&vectorHeap[bigger]);
		//printf("vectorHeap: %d\n",vectorHeap[index]);
		ShiftHeapDown(vectorHeap,bigger,n);
		//printf("vectorHeap: %d\n",vectorHeap[index]);


	}
	//printf("vectorHeap: %d\n",vectorHeap[index]);

}



void createHeapMax(int *vectorHeap, int n)
{ //this is equivalent to heapify
	int j = n/2;
	for(int i = j;i >= 1;i--){
		ShiftHeapDown(vectorHeap,i,n);
		//printvector(vectorHeap,n);
		
	}
	// what I am doing here in this tiny for
	// is doing the heap sort so that I cant 
	// degenerate the principal rule of Max Heap
	// the root node is the biggest one
	for(int i = n -1;i >= 0;i--){
		Swap(&vectorHeap[0],&vectorHeap[i]);
		ShiftHeapDown(vectorHeap,i,n);
	}
	printvector(vectorHeap,n);
	

}

int insert(int *vectorHeap, int new, int n)
{
	vectorHeap = (int*) realloc(vectorHeap,sizeof(int) * (n + 2));
	n = n + 1;
	vectorHeap[n] = new;
	ShiftHeapUp(vectorHeap,n);
	return n;
	
	
}



int main(){
	int *heap;
    int n;
    int entrada;
    int cont = 1;
    while(cont){
	    printf("Qual operação deseja realizar?\n");
	    printf("Digite 1 para criar heap de máximo\n");
	    printf("Digite 2 para ordenar\n");
	    printf("Digite 3 para inserir um novo elemento no Heap\n");
	    printf("Digite 4 para remover um elemento do Heap\n");
	    printf("Digigte 5 para remover um item e mudar sua prioridade\n");
	    printf("Digite 6 para sair\n");
	    scanf("%d",&entrada);

	    
	    
	    if(entrada == 1){
	    	printf("Insira o tamanho do vetor\n");
	    	scanf("%d",&n);
	    	heap = (int*) malloc((n + 1) * sizeof(int)); 
	    	srand(time(NULL));
	    	for(int i =0 ; i < n;++i)
	        	heap[i] = rand() % 100;
	        printf("Initial Heap: \n");
	        printvector(heap,n);

	        // Basically what I am doing here is creating a 
	        // priority list - and thats exactly what I need to implement Djikstra Algorithm and the Aˆ* algorithm
	        // 
	        printf("Max Heap:\n");
	    	createHeapMax(heap,n);
	    	
	    }
	    if(entrada == 3){
	    	int newValue;
	    	//3 stands for insert a new element
	    	printf("Digite o elemento a ser inserido: ");
	    	scanf("%d",&newValue);

	    	newValue = insert(heap,newValue,n);
	    	createHeapMax(heap,newValue);
	    	
	    	printvector(heap,newValue);

	    }
	    if(entrada == 6)
	    	break;



	}
	return 0;
}



