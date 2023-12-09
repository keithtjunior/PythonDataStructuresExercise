def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?
    
        >>> single_letter_count('Hello World', 'h')
        1
        
        >>> single_letter_count('Hello World', 'z')
        0
        
        >>> single_letter_count("Hello World", 'l')
        3
    """
    word_dict = {char.lower():0 for char in word}
    for char in word:
        word_dict[char.lower()] += 1
    return word_dict.get(letter.lower(), 0)
    # return word.lower().count(letter)