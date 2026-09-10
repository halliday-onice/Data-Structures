def rob(self, root) -> int:
        memo = {}
        def dfs_post_order(node): #left-right-current
            
            if not node: return 0 #get the things from the house, spear things
            if node in memo: return memo[node]
            # estou escolhendo pegar as coisas
            robbing_amount = node.val
            if node.left is not None:
                robbing_amount += dfs_post_order(node.left.left) + dfs_post_order(node.left.right)
            if node.right is not None:
                robbing_amount += dfs_post_order(node.right.left) + dfs_post_order(node.right.right)
            
            spare = dfs_post_order(node.left) + dfs_post_order(node.right)  
            results = max(spare, robbing_amount)
            memo[node] = results
            return results
        return dfs_post_order(root)