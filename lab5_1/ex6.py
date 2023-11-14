class LibraryItem:
    def __init__(self, title, author, appearance):
        self.title = title
        self.author = author
        self.appearance = appearance

    def __str__(self):
        return "Itemul pe care l ati ales are urmatoarele caracteristici: titlu: " + self.title + " autor: " + self.author + " an aparitie: " + str(self.appearance)

    def check_out(self, list):
        if self.title in list:
            return True
        else:
            return False

class Book(LibraryItem):
    def __init__(self, title, author, appearance, pages):
        LibraryItem.__init__(self, title, author, appearance)
        self.pages = pages

    def pages_number(self):
        return self.pages


class DVD(LibraryItem):
    def __init__(self, title, author, appearance, duration):
        LibraryItem.__init__(self, title, author, appearance)
        self.duration = duration

    def get_duration(self):
        return self.duration


class Magazine(LibraryItem):
    def __init__(self, title, author, appearance, number_episode):
        LibraryItem.__init__(self, title, author, appearance)
        self.number_episode = number_episode

    def episode(self):
        return self.number_episode


magazine = Magazine("Spider-man", "Lee", 2010, 10)
dvd = DVD("Cartea Junglei", "Mogli", 2005, 1.5)
book = Book("Data structures in python", "Mark", 2012, 150)
book2 = Book("Biologie", "Darvin", 1880, 1000)
list = ["Super-man", "Cartea Junglei", "Data structures in python"]
print(magazine.__str__())
print(dvd.get_duration())
print(book.check_out(list))
print(book2.check_out(list))
