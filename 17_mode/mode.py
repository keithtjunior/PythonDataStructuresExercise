def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    most_common = 0
    count = 0
    for num in nums:
        num_count = nums.count(num)
        if(num_count > count):
            count = num_count
            most_common = num
    return most_common
