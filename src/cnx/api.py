
import requests


class Chapter:
    def __init__(self, dictionary):
        self.root_url = 'https://archive.cnx.org/contents'
        setattr(self, 'has_subchapters', False)

        for k, v in dictionary.items():
            if k == 'contents':
                self.subchapters = []
                setattr(self, 'has_subchapters', True)
                for item in v:
                    chapter = Chapter(item)
                    self.subchapters.append(chapter)

            setattr(self, k, v)

    def text(self):
        r = requests.get(self.root_url + '/' + self.id + '.json')
        if r.status_code == 200:
            data = r.json()
            return data['content']
        else:
            raise Exception('There was a problem retrieving the text for that chapter')

    def __repr__(self):
        return '<title: {0} id: {1}>'.format(self.title, self.id)


class TableOfContent(object):
    def __init__(self, chapter_list):
        self.chapters = []
        for chapter_item in chapter_list:
            chapter = Chapter(chapter_item)
            self.chapters.append(chapter)

    def search(self, search_string):
        """ Search the table of contents tree for the title of a chapter. In the future do this recursively as chapters
        can have subchapters.
        :param search_string: the search string representing the title of the chapter
        :return: chapter
        """
        # TODO: Solve the chapter search with recursion. For now just doing the simplest thing possible.
        # Original query before subchapters
        # chapter = next((c for c in self.chapters if c.title.lower() == search_string.lower()), None)
        result = None
        for chapter in self.chapters:
            if chapter.title.lower() == search_string.lower():
                result = chapter
            elif chapter.has_subchapters:
                for subchapter in chapter.subchapters:
                    if subchapter.title.lower() == search_string.lower():
                        result = subchapter
        return result

    def __repr__(self):
        return self.chapters


class Book(object):
    books = {'biology': '',
             'sociology': '02040312-72c8-441e-a685-20e9333f3e1d'
             }

    def __init__(self, book_title):
        self.root_url = 'https://archive.cnx.org/contents/'
        self.book_title = book_title

        self._load_book(self.book_title)
        self._load_toc()

    def _load_book(self, book_title):
        try:
            self.uuid = self.books[book_title.lower()]
        except KeyError:
            raise Exception('That book was not found')
        #TODO: Add proper failures for invalid requests
        r = requests.get(self.root_url + self.uuid + '.json')

        if r.status_code == 200:
            # assign the rest of the book values as attributes
            for k, v in r.json().items():
                setattr(self, k, v)

        return self

    def _load_toc(self):
        self._toc = TableOfContent(self.tree['contents'])

        return

    def toc(self):
        return self._toc.chapters

    def chapter(self, chapter_title):
        c = self._toc.search(chapter_title)
        if c:
            return c
        else:
            raise Exception('That chapter was not found within the book')


def book(book_title):
    return Book(book_title)
