from Notebook.note_utils import Note
from os import listdir, mkdir, remove as delete_file
from os.path import exists
import datetime


def _parse_note(file_path):
    """Parses a note from the 'notes/' directory and loads it into a Note object"""
    with open(file_path, 'r') as f:
        content = f.readlines()
    for i, item in enumerate(content):
        content[i] = item.rstrip('\n')
    creation_date = datetime.datetime.strptime(content[1], '%m/%d/%Y').date()
    return Note(int(content[0]), content[2], content[3], creation_date=creation_date)


class Notebook:
    """This class is implemented so as to be an interface for all notes existing within the program"""
    def __init__(self):
        self._notes = dict()
        self._next_id = 1
        self._load_notes()
        self._get_next_id()

    def _load_notes(self):
        """Loads the notes existing in the /notes directory"""
        if not exists('notes'):
            mkdir('notes')
        files = listdir('notes')
        if files:
            for note in files:
                new_note = _parse_note('notes\\' + note)
                self._notes[new_note.identifier] = new_note
        return

    def _get_next_id(self):
        """Derives and sets the id that the next note should be if it is created"""
        if self._notes:
            self._next_id = max(self._notes, key=int) + 1
        return

    def add_note(self, tags, memo):
        """Adds a note to the notebook and writes it to the 'notes/' directory"""
        new_note = Note(self._next_id, tags, memo)
        self._notes[new_note.identifier] = new_note
        self._get_next_id()
        return

    def search_notes(self, param):
        """Searches all instances of notes within the object for matches of the string provided"""
        pass

    def delete_note(self, identifier):
        """Deletes a note via its ID. Returns true if found and deleted, false otherwise."""
        if identifier in self._notes:
            delete_file(self._notes[identifier].path)
            del self._notes[identifier]
        return False

    def edit_note(self, identifier):
        pass


if __name__ == '__main__':
    notebook = Notebook()
    notebook.add_note(['first'], 'this is the first note')
