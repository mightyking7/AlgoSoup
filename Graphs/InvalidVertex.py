'''
    Purpose:
        Raised if an operation expecting an INT had a value which was of the wrong type

    Parameters:
        Arguments to return as a message
'''
class InvalidVertex(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)