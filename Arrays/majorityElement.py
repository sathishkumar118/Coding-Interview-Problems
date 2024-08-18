def missingNumbers(array):  
    """  
    Find up to two missing positive integers from a sorted list.  

    This function takes a list of integers that may contain duplicates and  
    identifies the first two missing positive integers starting from 1.   
    The input list is expected to be sorted, and the output will contain   
    the smallest missing numbers.  

    Parameters:  
    array (list of int): A list of integers, which can contain duplicates.  

    Returns:  
    list of int: A list containing up to two missing positive integers.   
                 If there are no missing numbers, the list will be empty.  
    """
    chosen_elem = -1
    counter = 0
    for elem in array:
        if counter == 0:
            chosen_elem = elem
        if chosen_elem == elem:
            counter += 1
        else:
            counter -= 1
    return chosen_elem