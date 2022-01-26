from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__ (self, file_path):
        """creates an instance of WordFinder, accepts file_path"""
        self.words_list = []
        self.populate_words_list(file_path)
        print(f"{len(self.words_list)} words read")
        
    def populate_words_list (self, file_path):
        """populates words_list attribute with lines read from file, prints number of words read"""
        with open(file_path) as file:
            for line in file:
                self.words_list.append(line.strip())


    def random (self):
        """returns random word from words list"""
        return choice(self.words_list)

class SpecialWordFinder(WordFinder):
    """Random Word Finder: finds random words"""

    def populate_words_list(self, file_path):
        """populates word_list with lines read from file ignoring spaces, newlines, and comments"""
        with open(file_path) as file:
            for line in file:
                if(line.startswith("#") or line.isspace()):
                    pass
                else:
                    self.words_list.append(line.strip())

