def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    phrase_dict = {ltr:0 for ltr in phrase}
    for ltr in phrase:
        phrase_dict[ltr] += 1
    return phrase_dict