def sum_even_finonancci(limit):
    total_sum = 0
    a = 2 
    b = 8 
    total_sum = a


    while b <= limit:
        total_sum = total_sum + b
        next_even = b * 4 + a
        b = a
        b = next_even
      
    return total_sum


print(sum_even_finonancci(4000000))
