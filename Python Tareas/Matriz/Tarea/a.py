def column_sum(a): 
      
     return [sum(i) for i in zip(*lst)] 
      
lst = [[1, 5, 3], [2, 7, 8], [4, 6, 9]] 
print(column_sum(lst)) 