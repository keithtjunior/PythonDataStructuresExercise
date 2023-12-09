names = [
    {'first': 'Ada', 'last': 'Lovelace'},
    {'first': 'Grace', 'last': 'Hopper'},
]

def extract_full_names(people):
    """Return list of names, extracting from first+last keys in people dicts.

    - people: list of dictionaries, each with 'first' and 'last' keys for
              first and last names

    Returns list of space-separated first and last names.

        >>> names = [
        ...     {'first': 'Ada', 'last': 'Lovelace'},
        ...     {'first': 'Grace', 'last': 'Hopper'},
        ... ]

        >>> extract_full_names(names)
        ['Ada Lovelace', 'Grace Hopper']
    """

    return [" ".join(person.values()) for person in people]
    # return [person for person in people]
    # return [person for person in people for person in person.values()]
    # return [f"{f_name} {l_name}" for person in people for (f_name, l_name) in person]
    # return [name for person in people for name in person.values()]
    

