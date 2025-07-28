class libraryOfBabel:

    def __init__(self, page_length, dictionary):
        """
        Initializes the Library of Babel
        
        Parameters
        ---------
        page_length: int
            How long a page is
        dictionary: str
            String containing all the letters to be included
        """

        self.num_characters = len(dictionary)
        self.dictionary = [word for word in dictionary]

        self.page_length = page_length
        self.curr_page =[0]*self.page_length
    
    def get_current_page(self):
        """
        Returns a string of the current page
        
        Returns
        -------
        str
        """

        return "".join(self.dictionary[i] for i in self.curr_page)
    
    def flip_page(self, pages = 1):
        """
        Flips the page to the next one in the library

        Parameters
        ----------
        pages: int
            The number of pages to flip (optional)
        """

        self.curr_page[0] += pages

        pointer = 0
        remainder = 0
        while self.curr_page[pointer] >= self.num_characters:
            remainder = self.curr_page // self.num_characters
            self.curr_page[pointer] -= remainder * self.num_characters

            pointer += 1
            pointer %= self.page_length
