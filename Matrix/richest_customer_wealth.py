
'''

You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

 

Example 1:

Input: accounts = [[1,2,3],[3,2,1]]
Output: 6
Explanation:
1st customer has wealth = 1 + 2 + 3 = 6
2nd customer has wealth = 3 + 2 + 1 = 6
Both customers are considered the richest with a wealth of 6 each, so return 6.
Example 2:

Input: accounts = [[1,5],[7,3],[3,5]]
Output: 10
Explanation: 
1st customer has wealth = 6
2nd customer has wealth = 10 
3rd customer has wealth = 8
The 2nd customer is the richest with a wealth of 10.'''

def maximumWealth(self, accounts: list[list[int]]) -> int:
        
        clients = len(accounts)
        bank = len(accounts[0]) #conta coluna
        max_wealth = 0

        for i in range(clients):
            wealth = 0 # dessa forma, eu fixo a contagem de riqueza em cada linha, cada cliente, e vou somando
           
            for j in range(bank): # depois de percorrer as colunas todas, pergunto se eh o maximo
                wealth += accounts[i][j]
            if wealth > max_wealth:
                max_wealth = wealth
        return max_wealth