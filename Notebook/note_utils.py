import datetime


class Note:
    """
    Container class for the notes instantiated by the user.

    Attributes:
        identifier:int -- unique identifier of the note
        memo:string -- the actual content of the note
        tags:list<string> -- tags for easy searching
        creation_date:datetime.datetime -- date and time at which the note was created

    """

    def __init__(self, identifier, tags, memo, creation_date=None):
        self.identifier = identifier
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today() if creation_date is None else creation_date
        self.path = None
        self._write_note_file()

    def _write_note_file(self):
        """Writes a note to a text file in a format that is easily parsed."""
        payload = '\n'.join([str(self.identifier),
                            self.creation_date.strftime('%m/%d/%Y'),
                            ', '.join(self.tags),
                             self.memo])
        self.path = 'notes\\note_{}.txt'.format(self.identifier)
        with open(self.path, 'w') as f:
            f.write(payload)

    def _match(self, param):
        """Determines is the string 'param' could be referring to any content within the note"""
        pass


if __name__ == '__main__':
    Note('Test note.', ['test'])
