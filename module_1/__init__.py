"""A package.

Showing some different docstrings formats

https://realpython.com/documenting-python-code/#docstring-formats

"""

def get_dict_value(dictionary: dict, key: str) -> int:
    """Documentation using sphinx restructured text style.

    :parameter dictionary: The dict to look in
    :parameter key: the key to look for
    :returns: Value or 5
    """
    return dictionary.get(key,5)


def get_dict_value_2(dictionary: dict, key: str) -> int:
    """Documentation using sphinx and google style.

    Requires sphinx.ext.napoleon for correct generation
    https://www.sphinx-doc.org/en/master/usage/extensions/example_google.html#example-google
    https://google.github.io/styleguide/pyguide.html

    Args:
        dictionary (dict): The first parameter.
        key (str): The second parameter.

    Returns:
        int: The return value. True for success, False otherwise.

    """
    return dictionary.get(key,5)


def get_dict_value_3(dictionary: dict, key: str) -> int:
    """Get dict value using numpy style.

    Requires sphinx.ext.napoleon for correct generation
    https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard

    Parameters
    ----------
    dictionary : dict
        Give me a dict
    key : stre
        Give me a str

    Returns
    -------
    int
        Description of anonymous integer return value.

    """
    return dictionary.get(key,5)


def get_dict_value_4(dictionary: dict, key: str) -> int:
    """Get dict value using epytext style.

    Requires 'sphinx_epytext' and 'pip install sphinx-epytext'
    https://epydoc.sourceforge.net/epytext.html

    @param dictionary: This is a description of
        the parameter x to a function.
        Note that the description is
        indented four spaces.
    @param key: A key to search for
    @return: Return a value
    """
    return dictionary.get(key,5)
