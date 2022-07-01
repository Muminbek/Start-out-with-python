def find_max_recursively(S, n):                                        
    """Find the maximum element in a sequence S, of n elements.""" 
    if n == 1:  # reached the left most item                                   
        return S[n-1]                                                          
    else:                                                                      
        previous = find_max_recursively(S, n-1)                                
        current = S[n-1]                                                  
        if previous > current:                                                 
            return previous                                               
        else:                                                                  
            return current                                                     


if __name__ == '__main__':
    x = [45, 43, 67, 232, 66, 2, 6]                                                     
    print(find_max_recursively(x, len(x)))
