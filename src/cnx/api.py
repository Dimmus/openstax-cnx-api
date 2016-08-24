
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
    books = {u'concepts of biology': u'b3c1e1d2-839c-42b0-a314-e119a8aafbdd',
             u'calculus': u'9a1df55a-b167-4736-b5ad-15d996704270',
             u'biology': u'185cbf87-c72e-48f5-b51e-f14f21b5eabd',
             u'introduction to sociology': u'afe4332a-c97f-4fc4-be27-4e4d384a32d8',
             u'psychology': u'4abf04bf-93a0-45c3-9cbc-2cefd46e68cc',
             u'precalculus': u'fd53eae1-fa23-47c7-bb1b-972349835c3c',
             u'college physics for ap\xae courses': u'8d04a686-d5e8-4798-a27d-c608e4d0e187',
             u'principles of microeconomics for ap\xae courses': u'ca344e2d-6731-43cd-b851-a7b3aa0b37aa',
             u'calculus volume 2': u'1d39a348-071f-4537-85b6-c98912458c3c',
             u'u.s. history': u'a7ba2fb8-8925-4987-b182-5f4429d48daa',
             u'college physics': u'031da8d3-b525-429c-80cf-6c8ed997733a',
             u'prealgebra': u'caa57dab-41c7-455e-bd6f-f443cda5519c',
             u'calculus volume 3': u'a31cd793-2162-4e9e-acb5-6e6bbd76a5fa',
             u'calculus volume 1': u'8b89d172-2927-466f-8661-01abc7ccdba4',
             u'microeconomics': u'ea2f225e-6063-41ca-bcd8-36482e15ef65',
             u'principles of macroeconomics for ap\xae courses': u'33076054-ec1d-4417-8824-ce354efe42d0',
             u'introductory statistics': u'30189442-6998-4686-ac05-ed152b91b9de',
             u'chemistry': u'85abf193-2bd2-4908-8563-90b8a7ac8df6',
             u'anatomy & physiology': u'14fb4ad7-39a1-4eee-ab6e-3ef2482e3e22'}

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
