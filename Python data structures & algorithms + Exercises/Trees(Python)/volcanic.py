

def sortInsercted(volcanic, non_volcanic):
      comon_lst = []
      volc_list= []
      aux_volcanic_counter = None
      aux_non_volcanic_counter = None
      for i in range(len(volcanic)):
            print(f"i: {i}, volcanic[i]: {volcanic[i]}")
            aux_volcanic_counter = volcanic[i]
            for j in range(len(non_volcanic)):
                  if aux_volcanic_counter == non_volcanic[j]:
                        comon_lst.append(aux_volcanic_counter)
                  
      #print(f"common_lst: {comon_lst}")
      return sorted(comon_lst, reverse= True)

if __name__ == '__main__':
      volcanic=[7000,7000,12000,13000, 6900]
      non_volcanic = [6910, 7010, 7000, 12000, 18000, 15000, 10450]
      result = sortInserted(volcanic, non_volcanic)
      print(result)
""" 
7000
7000
12000
13000
6900

+++
6910
7010
7000
12000
18000
15000
10450

"""