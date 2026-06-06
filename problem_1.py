 def calculate_total_sum(limit):
    def sum_of_multiples(x, max_val):
       n = max_val // x
       return x * n * (n + 1) // 2 
                   
    sum_3  = sum_of_multiples(3, limit) 
    sum_5  = sum_of_multiples(5, limit)  
    sum_15 = sum_of_multiples(15, limit) 

    return sum_3 + sum_5 - sum_15
   
 print(calculate_total_sum(999))
