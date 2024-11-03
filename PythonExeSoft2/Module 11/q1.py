class Publication:
    def __init__(self, name):
        self.name = name

    def print_info(self):
        print(self.name, end=" ")

class Book(Publication):
    def __init__(self, name, author, pages):
        super().__init__(name)
        self.author = author
        self.pages = pages

    def print_info(self):
        super().print_info()
        print("(author " +self.author+", " + str(self.pages)+"pages)")

class Magazine(Publication):
    def __init__(self, name, editor):
        super().__init__(name)
        self.editor = editor

pub = []
pub.append(Magazine("Donald Duck", "Aki Hyy"))
pub.append(Book("Compartment No. 6", "Aki Hyy", 192))
for i in pub:
    i.print_info()