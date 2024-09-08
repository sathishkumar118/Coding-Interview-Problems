def sweetAndSavory(dishes, target):
    # Sort the dishes
    dishes.sort()
    
    # Separate sweet and savory dishes
    sweet_dishes = [dish for dish in dishes if dish < 0]
    savory_dishes = [dish for dish in dishes if dish > 0]
    
    # Pointers for the sweet and savory lists
    i, j = 0, len(savory_dishes) - 1
    best_pair = [0, 0]
    best_pair_sum = float('inf')
    
    # Use two-pointer approach to find the best pair
    while i < len(sweet_dishes) and j >= 0:
        curr_sum = sweet_dishes[i] + savory_dishes[j]
        diff = target - curr_sum
        
        if diff >= 0 and diff < best_pair_sum:
            best_pair_sum = diff
            best_pair = [sweet_dishes[i], savory_dishes[j]]
        
        if curr_sum < target:
            i += 1
        else:
            j -= 1
            
    return best_pair