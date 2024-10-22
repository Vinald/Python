class Book:
    def __init__(self, title):
        self.title = title

    # getter
    @property
    def title(self):
        print('Inside the getter')
        return self._title

    # setter
    @title.setter
    def title(self, new_title):
        print('Insider the setter')
        self._title = new_title


book = Book('Things fall apart')
print(book.title)

print(book.__dict__)
