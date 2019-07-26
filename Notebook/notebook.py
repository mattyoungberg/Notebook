class Notebook:
    """
    This class is implemented so as to be an interface for all notes existing within the program.

    Attributes:


    """
    def __init__(self):
        self.notes = {}

    def _load_notes(self):
        """Loads the notes existing in the /notes directory."""
        pass

    def _search_notes(self, param):
        """Searches all instances of notes within the object for matches of the string provided"""
        pass

    def _delete_note(self, identifier):
        pass