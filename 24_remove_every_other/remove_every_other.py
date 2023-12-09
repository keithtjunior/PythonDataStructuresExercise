lst = [1, 2, 3, 4, 5]

def remove_every_other(lst):
    """Return a new list of other item.

        >>> lst = [1, 2, 3, 4, 5]

        >>> remove_every_other(lst)
        [1, 3, 5]

    This should return a list, not mutate the original:

        >>> lst
        [1, 2, 3, 4, 5]
    """
    return [ele for ele in lst[::2]]
    return [lst[num] for num in range(0, len(lst), 2) for ele in lst]