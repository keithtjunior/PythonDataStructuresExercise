def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """
    for i, num1 in enumerate(nums[1:]):
        for num2 in nums:
            if nums[i] + num1 == goal:
                return (nums[i], num1)
            elif num1 + num2 == goal:
                return (num1, num2)
    return ()

    # return [(num, nums[i-1]) for i, num in enumerate(nums[1:]) if num + nums[i-1] == goal]
    # return [(num1 for num1 in nums) + (num2 for num2 in nums[1:])]
    # return [(num1, num2) for num1 in nums for num2 in nums[1:]]
    # return [zip(nums, nums[i+1:0]) for i in range(0, len(nums))]
    # return [i for i in range(0, len(nums)) for ele in nums if sum(nums[i], nums[i+1]) == goal]

