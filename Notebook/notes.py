import datetime
import uuid


def _parse_note(file):
    return identifier, memo, tag, creation_date


class Note:
    """
    Container class for the notes instantiated by the user.

    Attributes:
        identifier:int -- unique identifier of the note
        memo:string -- the actual content of the note
        tags:list<string> -- tags for easy searching
        creation_date:datetime.datetime -- date and time at which the note was created

    """

    def __init__(self, memo, tags):
        self.identifier = str(uuid.uuid4())
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.datetime.now()
        self._create_note()

    def _create_note(self):
        payload = ''
        payload += self.identifier + '\n' + \
                   str(self.creation_date) + '\n' + \
                   ', '.join(self.tags) + '\n\n' + \
                   self.memo
        with open(r'notes\{}.txt'.format(self.identifier), 'w') as f:
            f.write(payload)

    def _match(self, param):
        """
        This method will accept a string and can tell us whether a note matches the string without accessing the
        attributes directly. This way, if we want to modify the search parameter (to search tags instead of note
        contents, for example, or to make the search case-insensitive), we only have to do it in one place.

        Attributes:
            param:string -- string to search
            """
        pass


if __name__ == '__main__':
    Note('Test note.', ['test'])
