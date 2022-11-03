"""
Programming language class
"""


class ProgrammingLanguage:
    """Represent a programming language object """

    def __init__(self, name="", typing="Dynamic", reflection=True, year=0):
        """Initialise a ProgrammingLanguage instance"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Set string format for printing a ProgrammingLanguage instance"""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Determines if a programming language has dynamic typing"""
        return self.typing == "Dynamic"
