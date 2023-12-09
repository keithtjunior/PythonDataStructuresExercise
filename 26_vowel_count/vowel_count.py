def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """

    return {ltr:phrase.lower().count(ltr) for ltr in phrase.lower() if ltr in 'aeiou'}
    return {ltr:0 for ltr in phrase if ltr in 'aeiou'}
    return {char for char in phrase if char in 'aeiou'}