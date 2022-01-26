class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__ (self, file_path):
        """creates an instance of WordFinder, accepts file_path"""
        self.words_list = []
        self.populate_words_list(file_path)
        
    def populate_words_list (self, file_path):
        """populates words_list attribute with lines read from file, prints number of words read"""
        file = open(file_path) #refactor using with open instead
        for line in file:
            self.words_list.append(line)
        print(f"{len(self.words_list)} words read")
        file.close()

    

    def random (self, words_list):
