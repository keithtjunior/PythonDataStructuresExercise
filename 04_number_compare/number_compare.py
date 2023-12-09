def number_compare(a, b):
    """Report on whether a>b, b>a, or b==a
    
        >>> number_compare(1, 1)
        'Numbers are equal'
        
        >>> number_compare(-1, 1)
        'Second is greater'
        
        >>> number_compare(1, -2)
        'First is greater'
    """
    if (type(a) == int or type(a) == float) and (type(b) == int or type(b) == float):
        if a > b:
            return 'First is greater'
        elif b > a:
            return 'Second is greater'
        else:
            return 'Numbers are equal'
    return 'Invalid entries'