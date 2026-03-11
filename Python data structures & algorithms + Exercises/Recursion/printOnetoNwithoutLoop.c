
//Initial Template for C

#include <stdio.h>


// } Driver Code Ends
//User function Template for C

void printNos(int N)
{

    if(N == 0){
        return;

    }
    N--;
    printNos(N);
    printf("%d ", N + 1);



}

//{ Driver Code Starts.
/* Driver program to test printNos */
int main()
{
    printNos(10);
    printf("\n");



    return 0;
}

// } Driver Code Ends
