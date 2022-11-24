"""
Band class

A band is a list/ collection of musicians
Each musician has a set of guitars/instruments
"""


class Band:
    """Band class for storing members of a band"""

    def __init__(self, name=""):
        """Construct a Band class with a name and empty musician list"""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band"""
        musician_strings = [str(musician) for musician in self.musicians]
        return f"{self.name} ({', '.join(musician_strings)})"

    def add(self, musician):
        """Add a musician to the Band"""
        self.musicians.append(musician)

    def play(self):
        """Runs through list of musicians and plays their instruments"""
        musicians_playing = [musician.play() for musician in self.musicians]
        return '\n'.join(musicians_playing)
