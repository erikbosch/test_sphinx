# Example taken from https://www.programiz.com/python-programming/docstrings
class Dog:
    """
    A class to represent a Dog.

    ...

    Attributes
    ----------
    name : str
        first name of the Dog
    surname : str
        family name of the Dog
    age : int
        age of the Dog

    Methods
    -------
    info(additional=""):
        Prints the Dog's name and age.
    """

    def __init__(self, name, surname, age):
        """
        Constructs all the necessary attributes for the Dog object.

        Parameters
        ----------
            name : str
                first name of the Dog
            surname : str
                family name of the Dog
            age : int
                age of the Dog
        """

        self.name = name
        self.surname = surname
        self.age = age

    def info(self, additional=""):
        """
        Prints the Dog's name and age.

        If the argument 'additional' is passed, then it is appended after the main info.

        Parameters
        ----------
        additional : str, optional
            More info to be displayed (default is None)

        Returns
        -------
        None
        """

        print(f'My name is {self.name} {self.surname}. I am {self.age} years old.' + additional)