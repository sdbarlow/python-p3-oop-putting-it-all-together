#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count = 0):
        self.title = title
        self.page_count = page_count
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
    def get_count(self):
        print("getting page count")
        return self._count
    def set_count(self, count):
        if isinstance(count, int):
            print("setting page count")
            self._count = count
        else:
            print("page_count must be an integer")
    page_count = property(get_count, set_count)


sethsbook = Book("green eggs and ham", 50)
sethsbook.turn_page()

